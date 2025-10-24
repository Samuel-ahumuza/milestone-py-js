import sys

# Define a constant for the power supply buffer
PSU_BUFFER_W = 50

# --- 7.1 Object-Oriented Design: Component Modeling ---

class Component:
    """Base class for all PC components."""
    def __init__(self, component_id, component_type, score, cost, spec1, spec2):
        self.id = component_id
        self.type = component_type
        # Ensure numerical values are correctly cast and non-negative
        try:
            self.performance_score = int(score)
            self.cost = int(cost)
        except ValueError:
            # Handle case where score or cost are non-numeric - treat as invalid/unusable
            print(f"Error: Non-numeric score or cost for {component_id}", file=sys.stderr)
            self.performance_score = -1 # Sentinel value
            self.cost = float('inf')    # Effectively disqualifies the component
            
        # Ensure specs are stored as strings, even if they represent a number
        self.spec1 = str(spec1)
        self.spec2 = str(spec2)

    def __str__(self):
        return f"{self.type}({self.id}): Score={self.performance_score}, Cost={self.cost}"

class CPU(Component):
    def __init__(self, component_id, score, cost, socket, tdp):
        # Convert TDP to integer, handling potential errors
        try:
            tdp_int = int(tdp)
            if tdp_int < 0: tdp_int = 0
        except ValueError:
            tdp_int = 0 # Default to 0 if non-numeric
            
        super().__init__(component_id, "CPU", score, cost, socket, tdp_int)
        self.socket = self.spec1
        self.tdp = self.spec2 # Stored as int

class Motherboard(Component):
    def __init__(self, component_id, score, cost, socket, ram_type):
        super().__init__(component_id, "Motherboard", score, cost, socket, ram_type)
        self.socket = self.spec1
        self.ram_type = self.spec2

class GPU(Component):
    def __init__(self, component_id, score, cost, _, tdp):
        # Convert TDP to integer, handling potential errors
        try:
            tdp_int = int(tdp)
            if tdp_int < 0: tdp_int = 0
        except ValueError:
            tdp_int = 0
            
        super().__init__(component_id, "GPU", score, cost, "-", tdp_int)
        self.tdp = self.spec2 # Stored as int

class RAM(Component):
    def __init__(self, component_id, score, cost, ram_type, _):
        super().__init__(component_id, "RAM", score, cost, ram_type, "-")
        self.ram_type = self.spec1

class PSU(Component):
    def __init__(self, component_id, score, cost, wattage, _):
        # Convert wattage to integer, handling potential errors
        try:
            wattage_int = int(wattage)
            if wattage_int < 0: wattage_int = 0
        except ValueError:
            wattage_int = 0
            
        super().__init__(component_id, "PSU", score, cost, wattage_int, "-")
        self.wattage = self.spec1 # Stored as int

# --- 7.1 Object-Oriented Design: PCBuild Logic ---

class PCBuild:
    """Represents a potential PC build kit and handles validation."""
    
    def __init__(self, kit_id, components):
        """
        Initializes the build.
        :param kit_id: The ID of the kit (e.g., "kit_A").
        :param components: A dictionary of the 5 Component objects (CPU, Motherboard, etc.).
        """
        self.kit_id = kit_id
        self.components = components
        self.cpu = components.get("CPU")
        self.motherboard = components.get("Motherboard")
        self.gpu = components.get("GPU")
        self.ram = components.get("RAM")
        self.psu = components.get("PSU")

        # Calculate scores and costs
        if len(components) == 5:
            self.total_cost = sum(c.cost for c in components.values())
            self.total_performance_score = sum(c.performance_score for c in components.values())
        else:
            # If components are missing, cost is infinite, score is 0
            self.total_cost = float('inf')
            self.total_performance_score = 0
            
    def is_compatible(self):
        """Checks all 3 compatibility rules."""
        
        # 0. Check for existence (handled by constructor, but a quick check)
        if len(self.components) != 5:
            # This should only happen if a component ID was missing from inventory
            return False 
        
        # 1. CPU-Motherboard Socket Match (case-sensitive)
        # cpu.socket (spec1) == motherboard.socket (spec1)
        if self.cpu.socket != self.motherboard.socket:
            return False
            
        # 2. RAM-Motherboard Type Match (case-sensitive)
        # ram.ram_type (spec1) == motherboard.ram_type (spec2)
        if self.ram.ram_type != self.motherboard.ram_type:
            return False

        # 3. PSU Wattage Sufficient: psu.wattage >= (cpu.TDP + gpu.TDP + 50)
        # Note: TDPs are stored as integers (self.spec2)
        required_wattage = self.cpu.tdp + self.gpu.tdp + PSU_BUFFER_W
        if self.psu.wattage < required_wattage:
            return False
            
        return True # All checks passed

    def is_valid_and_affordable(self, budget):
        """Checks compatibility AND budget."""
        is_affordable = self.total_cost <= budget
        return self.is_compatible() and is_affordable

# --- 7.2 Data Structures & Main Logic ---

def parse_input():
    """Reads all input from standard input and processes it."""
    
    # Read Budget (B)
    try:
        total_budget = int(sys.stdin.readline().strip())
    except:
        return None, None, None # Invalid budget, stop
        
    # Read Number of Components (P)
    try:
        p_count = int(sys.stdin.readline().strip())
    except:
        p_count = 0
        
    # Read Component Inventory
    # 7.2 Data Structure: Use a dictionary for O(1) lookups
    inventory = {} # key: component_id, value: Component object
    
    for _ in range(p_count):
        line = sys.stdin.readline().strip()
        if not line: continue
        parts = line.split()
        
        if len(parts) < 6: continue # Skip malformed lines

        component_id, c_type, score, cost, spec1, spec2 = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
        
        # Component Factory pattern (simplified)
        component = None
        if c_type == "CPU":
            component = CPU(component_id, score, cost, spec1, spec2)
        elif c_type == "Motherboard":
            component = Motherboard(component_id, score, cost, spec1, spec2)
        elif c_type == "GPU":
            component = GPU(component_id, score, cost, spec1, spec2)
        elif c_type == "RAM":
            component = RAM(component_id, score, cost, spec1, spec2)
        elif c_type == "PSU":
            component = PSU(component_id, score, cost, spec1, spec2)
            
        if component and component.performance_score != -1: # Only add if successfully parsed
            inventory[component_id] = component
            
    # Read Number of Build Kits (K)
    try:
        k_count = int(sys.stdin.readline().strip())
    except:
        k_count = 0
        
    # Read Build Kits
    build_kits = [] # 7.2 Data Structure: Use a list to store kit lines in order
    for _ in range(k_count):
        line = sys.stdin.readline().strip()
        if line:
            build_kits.append(line.split())
            
    return total_budget, inventory, build_kits

def find_best_build(total_budget, inventory, build_kits):
    """
    Processes all build kits, validates them, and finds the best one.
    7.3 Algorithm Design: Tracking the best build.
    """
    
    # Initial state for tracking the best build
    best_score = 0
    best_kit_id = "NONE"

    # Define the expected component types in order of the input line
    component_types = ["CPU", "Motherboard", "GPU", "RAM", "PSU"]
    
    # 7.3 Time Complexity: O(K) loop over K build kits
    for kit_line in build_kits:
        if len(kit_line) != 6: continue # Malformed kit line

        kit_id = kit_line[0]
        component_ids = kit_line[1:]
        
        # 7.4 Error Handling: Check for missing components (O(1) lookup)
        kit_components = {}
        all_exist = True
        
        for i, comp_id in enumerate(component_ids):
            component = inventory.get(comp_id) # O(1) lookup
            if not component:
                all_exist = False
                break
            
            # Check for correct type (as per the problem statement, CPU is first, etc.)
            expected_type = component_types[i]
            if component.type != expected_type:
                # This should ideally not happen if input adheres to the format spec
                # but is a good safeguard against malformed data.
                all_exist = False 
                break 

            kit_components[expected_type] = component
        
        # 5.3 & 5.4 Invalid Component References: Skip if any component is missing
        if not all_exist:
            continue
            
        # Create and validate the build
        build = PCBuild(kit_id, kit_components)
        
        # 2.4 Goal: Check Affordability and Compatibility
        if build.is_valid_and_affordable(total_budget):
            
            # 2.4 Goal & 5.2 Ties: If valid, compare score with current best
            if build.total_performance_score > best_score:
                best_score = build.total_performance_score
                best_kit_id = kit_id
            # Note on Ties (5.2): If scores are equal, the first one encountered (due to
            # iterating through `build_kits` list) is kept, which satisfies the tie-breaking rule.
                
    return best_score, best_kit_id

# --- Execution ---

def main():
    """Main function to run the script."""
    # 1. Parse the budget and component inventory
    total_budget, inventory, build_kits = parse_input()
    
    if total_budget is None:
        # Handle case where initial budget read failed
        print("Maximum Score: 0")
        print("Best Build: NONE")
        return
        
    # 2. Process kits and find the best
    max_score, best_kit_id = find_best_build(total_budget, inventory, build_kits)
    
    # 3. Output the result
    print(f"Maximum Score: {max_score}")
    print(f"Best Build: {best_kit_id}")
    
if __name__ == "__main__":
    # The script execution assumes input is piped or typed via standard input.
    main()
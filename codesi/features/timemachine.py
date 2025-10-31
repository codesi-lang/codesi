import copy
from ..interpreter.runtime import CodesiFunction, CodesiClass

class CodesiTimeMachine:
    """World's first time-travel debugger for a programming language"""
    
    def __init__(self):
        self.snapshots = []
        self.enabled = False
        self.current_step = 0
        self.limit_warning_shown = False  
    
    def enable(self, max_snapshots=100):
        """Enable time machine with configurable snapshot limit"""
        
        if self.enabled and self.snapshots:
            print(f"Time Machine restarted! Pichle {len(self.snapshots)} snapshots clear hogye.")
        
        self.enabled = True
        self.snapshots = []
        self.current_step = 0
        self.max_snapshots = max_snapshots
        self.limit_warning_shown = False
        print(f"Time Machine activated! (Max snapshots: {self.max_snapshots})")
        return None
    
    def disable(self):
        """Disable time machine and clear snapshots"""
        if not self.enabled:
            print("Time Machine pehle se off hai!")
            return None
        
        snapshot_count = len(self.snapshots)
        self.enabled = False
        self.snapshots = []
        self.current_step = 0
        self.limit_warning_shown = False
        
        print(f"Time Machine deactivated! ({snapshot_count} snapshots cleared)")
        return None

    def status(self):
        """Show time machine status"""
        if self.enabled:
            print(f"  Time Machine: ON")
            print(f"   Max snapshots: {self.max_snapshots}")
            print(f"   Current snapshots: {len(self.snapshots)}")
            print(f"   Current step: {self.current_step}")
        else:
            print(f"  Time Machine: OFF")
        return None    

    def take_snapshot(self, scope, line_info):
        if not self.enabled:
            return
        
        
        if len(self.snapshots) >= self.max_snapshots:
           
            if not self.limit_warning_shown:
                print(f"\n   Time Machine Limit Reached!")
                print(f"   Current limit: {self.max_snapshots} snapshots")
                print(f"     Tip: Use time_machine_on(max=500) for more snapshots")
                print(f"   Oldest snapshots silently remove ho jayenge.\n")
                self.limit_warning_shown = True  
            
            self.snapshots.pop(0)  
            if self.current_step > 1:
                self.current_step -= 1
        
        # Create user variables dict from current scope
        user_vars = {}
        for k, v in scope.items():
            # Skip built-in functions (but keep CodesiFunction and CodesiClass)
            if callable(v) and not isinstance(v, (CodesiFunction, CodesiClass)):
                continue
            
            # Deep copy for nested structures (production-grade solution)
            try:
                if isinstance(v, (list, dict)):
                    # Use deepcopy for nested arrays/objects
                    user_vars[k] = copy.deepcopy(v)
                elif isinstance(v, (CodesiFunction, CodesiClass)):
                    # Don't copy functions/classes - store reference
                    user_vars[k] = v
                else:
                    # For primitives (int, float, str, bool, None), direct assignment is fine
                    user_vars[k] = v
            except Exception:
                # Fallback: if deepcopy fails for any reason, use reference
                # This handles edge cases like objects with special attributes
                user_vars[k] = v
        
        snapshot = {
            'step': len(self.snapshots) + 1,
            'variables': user_vars,
            'info': line_info
        }
        self.snapshots.append(snapshot)
        self.current_step = len(self.snapshots)    

    def go_back(self, steps=1):
        if not self.snapshots:
            return "Time machine mein koi snapshot nahi hai! Ya fir Time Machine Off hai"
        
        self.current_step = max(1, self.current_step - steps)
        return self.current_step - 1
    
    def go_forward(self, steps=1):
        if not self.snapshots:
            return "Time machine mein koi snapshot nahi hai! Ya fir Time Machine Off hai"
        
        self.current_step = min(len(self.snapshots), self.current_step + steps)
        return self.current_step - 1
    
    def get_snapshot(self, index):
        """Get snapshot data without printing"""
        if not self.snapshots or index < 0 or index >= len(self.snapshots):
            return None
        return self.snapshots[index]

    def _show_snapshot(self, index):
        """Display snapshot info"""
        snap = self.get_snapshot(index)
        if not snap:
            return "Invalid step!"
        
        output = f"\nTime Travel: Step {snap['step']}/{len(self.snapshots)}\n"
        output += f"{snap['info']}\n"
        output += "Variables at this point:\n"
        
        for var, val in snap['variables'].items():
            if not var.startswith('_') and not callable(val):
               
                if isinstance(val, list):
                    formatted = '[' + ', '.join(str(v) for v in val) + ']'
                    output += f"   {var} = {formatted}\n"
                else:
                    output += f"   {var} = {val}\n"
        
        return output
    
    def show_all_steps(self):
        if not self.snapshots:
            return "Time machine mein koi snapshot nahi hai! Ya fir Time Machine Off hai"
        
        output = "\nComplete Execution Timeline:\n" + "="*60 + "\n"
        for snap in self.snapshots:
            output += f"Step {snap['step']}: {snap['info']}\n"
        output += "="*60
        return output

time_machine = CodesiTimeMachine()

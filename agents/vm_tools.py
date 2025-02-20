from core.types import ParallelsAIAgent, Result


class VMToolsAgent(ParallelsAIAgent):
    def __init__(self):
        super().__init__(
            name="VM Tools Agent",
            instructions="I help manage virtual machines with basic operations.",
            functions=[self.get_vm_info, self.check_vm_status],
        )

    def get_vm_info(self, vm_id: str) -> Result:
        """Get basic information about a VM"""
        # This is just a mock implementation
        return Result(
            value=f"Getting info for VM {vm_id}", context_variables={"vm_id": vm_id}
        )

    def check_vm_status(self, vm_id: str) -> Result:
        """Check if a VM is running"""
        # This is just a mock implementation
        return Result(
            value=f"Checking status for VM {vm_id}", context_variables={"vm_id": vm_id}
        )

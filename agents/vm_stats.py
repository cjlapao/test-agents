from core.types import ParallelsAIAgent, Result


class VMStatsAgent(ParallelsAIAgent):
    def __init__(self):
        super().__init__(
            name="VM Statistics Agent",
            instructions="I provide detailed statistics about virtual machines.",
            functions=[self.get_vm_resources, self.get_vm_performance],
        )

    def get_vm_resources(self, vm_id: str) -> Result:
        """Get resource usage for a VM"""
        # This is just a mock implementation
        return Result(
            value=f"Getting resource usage for VM {vm_id}",
            context_variables={"vm_id": vm_id},
        )

    def get_vm_performance(self, vm_id: str) -> Result:
        """Get performance metrics for a VM"""
        # This is just a mock implementation
        return Result(
            value=f"Getting performance metrics for VM {vm_id}",
            context_variables={"vm_id": vm_id},
        )

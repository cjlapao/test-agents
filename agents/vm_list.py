from core.types import ParallelsAIAgent, Result


class VMStatsAgent(ParallelsAIAgent):
    def __init__(self):
        super().__init__(
            name="VM List Agent",
            instructions="I provide a list of virtual machines or a specific virtual machine.",
            functions=[self.get_vm_list],
        )

    def get_vm_list(self) -> Result:
        """Get a list of virtual machines or a specific virtual machine"""
        # This is just a mock implementation
        return Result(
            value="""
            [
              {
                "id": "1",
                "name": "VM 1",
                "status": "running",
                "ip": "192.168.1.1",
                "mac": "00:00:00:00:00:00"
              },
              {
                "id": "2",
                "name": "VM 2",
                "status": "stopped",
                "ip": "192.168.1.2",
              }
            ]
            """,
        )

    def get_vm_performance(self, vm_id: str) -> Result:
        """Get performance metrics for a VM"""
        # This is just a mock implementation
        return Result(
            value=f"""
            {
                "id": "1",
                "name": "VM 1",
                "status": "running",
                "ip": "192.168.1.1",
                "cpu": 50,
                "memory": 1024,
                "disk": 10240,
                "network": "192.168.1.1/24"
            }
            """,
            context_variables={"vm_id": vm_id},
        )

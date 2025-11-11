from one_eval.core.node_base import BaseNode

class NL2BenchNode(BaseNode):
    def run(self, state):
        self.log("Searching benchmarks...")
        state.update(benches=["Bench-A"])
        return state

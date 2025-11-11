from one_eval.core.node import BaseNode

class EvalNode(BaseNode):
    def run(self, state):
        self.log(f"Evaluating {state.benches}")
        state.update(eval_results={"Bench-A": 0.95})
        return state

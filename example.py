import argparse
from tot.methods.bfs import solve, naive_solve
from tot.tasks.game24 import Game24Task

args = argparse.Namespace(backend='llama3', temperature=0.7, task='game24', naive_run=False, prompt_sample=None, method_generate='propose',
                          method_evaluate='value', method_select='greedy', n_generate_sample=1, n_evaluate_sample=3, n_select_sample=5)

# args = argparse.Namespace(backend='llama3', temperature=0.7, task='game24', naive_run=True, prompt_sample='cot', method_generate='propose',
#                           method_evaluate='value', method_select='greedy', n_generate_sample=1, n_evaluate_sample=3, n_select_sample=5)

task = Game24Task()
ys, infos = solve(args, task, 903)
# ys, infos = naive_solve(args, task, 980)
print("LLM Reply: ", ys)
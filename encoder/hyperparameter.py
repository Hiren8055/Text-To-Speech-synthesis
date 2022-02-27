# from sklearn.metrics import accuracy_score
# import optuna

# # learning rate
# # Optimizer

# # optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate_init) 




# def objective(trial):
#     # model = 
#     optimzier_name = trial.suggest_categorial("optimizer",["Adam","RMSprop","SGD"])
#     lr = trial.suggest_float("lr",1e-5,1e-1, log=True)
#     optimizer = getattr(optim,optimzier_name)(model.parmeters(),lr=lr)
#     epochs = 100
#     for epoch in range(epochs):
#         trial.report(accuracy,epoch)
#         if trial.should_prune():
#             raise optuna.exceptions.TrialPruned()
#     return accuracy 


from hyperopt import hp, fmin , tpe, Trials




def optimize(params,x,y):
    # params = dict(zip(param_names,params))










param_space ={
    "learning_rate": hp.uniform(),
    "optimizer": hp.choice()
}    
# quniform - round(uniform(low,high)/q)*q
# early stopping "criterion" : hp.choice("criterion","gini","entropy")

# param_names = ["learning_rate","optimizer"]

optimization_function = partial(optimize,x=,y=)
trials = Trials()
results = fmin(
fn = optimization_function,
space =param_space,
algo=tpe.suggest,
max_evals = 15,
trials =trials
)
print(results)


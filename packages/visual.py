class Visualize:
    
    def __init__(self, df = None):
        self.df = df
        
        
    def Freq_count(self,filename="plot.png"):
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set_theme(style="darkgrid")
        import pandas as pd
        tips = sns.load_dataset("tips")
        tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
        sns.catplot(data=tips, x="day", y="total_bill", hue="weekend", kind="box")
        plt.show()
        plt.savefig(filename, bbox_inches="tight")
        
        
# obj = Visualize()
# obj.Freq_count()
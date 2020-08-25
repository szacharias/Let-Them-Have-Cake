import seaborn as sns # for data visualization
import matplotlib.pyplot as plt # for data visualization
import pandas as pd # for data analysis
import plotly.express as px

def get_df(data_base_dir , weekly_driving_history ):
    base_df = pd.read_csv(data_base_dir + weekly_driving_history[0])
    for week_data_index in range(1, len(weekly_driving_history)): 
        print(data_base_dir + weekly_driving_history[week_data_index])
        new_df = pd.read_csv(data_base_dir + weekly_driving_history[week_data_index])
        base_df = pd.concat([base_df, new_df], ignore_index = True, sort = False)
    return base_df


def clean_dataframe(df):
    df = df.drop(["Driver Name" , "Phone Number" , "Email", "Trip ID", "Type"],axis = 1)
    df = df.replace({'\$':''}, regex = True) 
    df = df.astype({'Base Fare': 'float64','Tip': 'float64','Surge': 'float64',
                    'Trip Supplement': 'float64','Quest Promotion': 'float64',
                    'Total': 'float64'}).fillna(0)
    df["Date/Time"] = pd.to_datetime(df["Date/Time"])
    df = df.sort_values(['Date/Time']).reset_index(drop = True)
    
    return df

def corr_plot(weekly_data ): 
    testing_week_corr_data = weekly_data.drop(["Quest Promotion", "Date/Time"],axis = 1)
    corr_columns = testing_week_corr_data.columns

    corr = testing_week_corr_data.corr()

    annot_kws={'fontsize':10, 
               'fontstyle':'italic',  
               'color':"k",
               'alpha':0.6, 
               'verticalalignment':'center',
               'horizontalalignment':'center'}

    plt.figure(figsize = (16,8))
    sns.heatmap( corr, annot=True,linewidth = 0, cmap="coolwarm",annot_kws= annot_kws )
    # sns.ylabel(rotation = 90)
    plt.savefig("./img/CorrelationMap.png")


    ################### Deprecated Heatmap ###################
    # fig = px.imshow(corr,
    #                 labels=dict(x="Day of Week", y="Time of Day"),
    #                 x=corr_columns,
    #                 y=corr_columns
    #                )
    # fig.update_xaxes(side="top")
    # plt.savefig("CorrelationMap.png")
    # fig.show()
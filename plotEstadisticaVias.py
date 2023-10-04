##ALL THIS CODE WILL NOT WORK WITHOUT THE OTHER PART (QUERY AND DB CONNECTION) IT'S JUST THE PLOT PART
#
#The plot is about the mount of transactions for every road toll from an specific toll station. 
#
#The green color is for the movements readed by the antenna, the red for the manuals and de orange for the emergencys
#
#Then, under the x-axis you have the % of reading rate of every antenna. if the % < 70 ill be red and if the % > 85 ill be green  

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd




    
date_ini_start = 'insertYourDateIni'
date_ini_end   = 'insertYourDateEnd'
dealer_id      = 2 

def plot_data(df, date_ini_start, date_ini_end, save_path = "output"):

    plt.figure(figsize=(12, 8))
    station_name = df['station_name'].iloc[0]


    bars1 = plt.bar(bar_positions, df['total_movimientos_manuales'   ], label='Movimientos Manuales', color='red')
    bars2 = plt.bar(bar_positions, df['total_movimientos_automaticos'], bottom=df['total_movimientos_manuales'], label='Movimientos Automaticos', color='green')
    bars3 = plt.bar(bar_positions, df['total_movimientos_emergencia' ], bottom=df['total_movimientos_manuales'] + df['total_movimientos_automaticos'], label='Movimientos Emergencia', color='orange')

    for i, bar in enumerate(bars1):
        yval = bar.get_height()
        if yval != 0:
            plt.text(bar.get_x() + bar.get_width()/2, yval - (0.8*yval), f'Mov: {round(yval,2)}', ha='center', va='bottom', color='black', fontsize=10)

    for i, bar in enumerate(bars2):
        yval = bar.get_height() + bars1[i].get_height()
        if yval-bars1[i].get_height() != 0:
            plt.text(bar.get_x() + bar.get_width()/2, yval - (0.3*yval),  f'Mov: {round(yval-bars1[i].get_height(),2)}', ha='center', va='bottom', color='black', fontsize=10)

    for i, bar in enumerate(bars3):
        yval = bar.get_height() + bars1[i].get_height() + bars2[i].get_height()
        if bar.get_height() != 0:
            plt.text(bar.get_x() + bar.get_width()/2, yval - (0.9*bar.get_height()), f'Mov: {round(bar.get_height(),2)}', ha='center', va='bottom', color='black', fontsize=10)
        

        tasa = df.iloc[i]['tasa_lectura']
        totalMov = df.iloc[i]['total_movimientos']

        if tasa > 85:
            color = 'green'
        elif tasa < 70:
            color = 'red'
        else:
            color = 'black'


        plt.text(bar.get_x() + bar.get_width()/2, -0.1*max(df['total_movimientos']), f'% {round(tasa,2)}', ha='center', va='bottom', color=color, fontsize=10)
        plt.text(bar.get_x() + bar.get_width()/2, -0.07*max(df['total_movimientos']), f'Tot: {totalMov}', ha='center', va='bottom', color='black', fontsize=10)


    legend_elements = [ mlines.Line2D([0], [0], label=f'Fecha inicio: {date_ini_start}',color='white' ),
                        mlines.Line2D([0], [0], label=f'Fecha fin: {date_ini_end}'     ,color='white' ),
                        mlines.Line2D([0], [0], label='Movimientos Manuales'           ,color='red'   ),
                        mlines.Line2D([0], [0], label='Movimientos Automaticos'        ,color='green' ),
                        mlines.Line2D([0], [0], label='Movimientos Emergencia'         ,color='orange'),
                        ]


    plt.xticks(bar_positions, df['lane'])

    plt.xlabel('Vias:', loc='left',labelpad=-11)
    plt.ylabel('Total Movimientos')
    plt.title(f'Total Movimientos y Tasa Lectura por vía ({station_name})')
    plt.legend(handles=legend_elements)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.savefig(f'{save_path}.jpg', dpi=300, bbox_inches='tight')
    plt.show()

# print(df)
plot_data(df, date_ini_start, date_ini_end,"yourRoutePathToSaveTheJPG")
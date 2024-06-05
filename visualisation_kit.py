import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_categorical_distributions(
    df: pd.DataFrame,
    categorical_cols: list) -> None:

    num_cols = 3
    num_rows = (len(categorical_cols) + num_cols - 1) // num_cols
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 15))

    for i, ax in zip(categorical_cols, axes.flatten()):
        sns.countplot(x=df[i], ax=ax, order=df[i].value_counts().index)
        ax.set_title(f"{i}")
        ax.set_xlabel("")
        ax.set_ylabel("Count")
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True)

        total = float(len(df[i]))
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{(height/total)*100:.2f}%', 
                        (p.get_x() + p.get_width() / 2., height), 
                        ha='center', va='bottom')

    plt.suptitle('Distributions of Categorical Variables', size=20, y=1.02)
    plt.tight_layout()
    plt.show()

    return None

def plot_target_distribution(
    df: pd.DataFrame,
    categorical_cols: list,
    target_col: str = 'y') -> None:

    categorical_cols_temp = [col for col in categorical_cols if col != target_col]

    num_cols = 2
    num_rows = (len(categorical_cols_temp) + num_cols - 1) // num_cols
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(20, 30))

    for i, category in enumerate(categorical_cols_temp):
        category_distribution = df.groupby(category)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)
        category_distribution = category_distribution.sort_values(by='yes', ascending=False)
        
        row = i // num_cols
        col = i % num_cols

        ax = category_distribution.plot(kind='bar', stacked=True, ax=axes[row, col])
        ax.set_title(f"Distribution of target in '{category}'")
        ax.set_xlabel(category)
        ax.set_ylabel('Percentage')
        ax.legend().remove()
        ax.tick_params(axis='x', rotation=45)
        
        for p in ax.patches:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy()
            if height > 0:
                ax.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', shadow=True, prop={'size': 16})

    plt.suptitle('The Distribution of Target "y" Across Categorical Variables', size=20, y=1)
    plt.tight_layout()
    plt.show()

    return None

def compare_categorical_distributions(
    campaign_group: pd.DataFrame,
    control_group: pd.DataFrame,
    categorical_cols: list) -> None:
    
    num_rows = len(categorical_cols)
    num_cols = 2

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 25))

    for i, col in enumerate(categorical_cols):
        sns.countplot(x=col, data=campaign_group, ax=axes[i, 0], order=campaign_group[col].value_counts().index)
        axes[i, 0].set_title(f"Campaign Group - {col}")
        axes[i, 0].set_xlabel("")
        axes[i, 0].set_ylabel("Count")
        axes[i, 0].tick_params(axis='x', rotation=45)
        axes[i, 0].grid(True)
        
        total_campaign = float(len(campaign_group[col]))
        for p in axes[i, 0].patches:
            height = p.get_height()
            axes[i, 0].annotate(f'{(height/total_campaign)*100:.2f}%', 
                                (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='bottom')

        sns.countplot(x=col, data=control_group, ax=axes[i, 1], order=control_group[col].value_counts().index)
        axes[i, 1].set_title(f"Control Group - {col}")
        axes[i, 1].set_xlabel("")
        axes[i, 1].set_ylabel("Count")
        axes[i, 1].tick_params(axis='x', rotation=45)
        axes[i, 1].grid(True)
        
        total_control = float(len(control_group[col]))
        for p in axes[i, 1].patches:
            height = p.get_height()
            axes[i, 1].annotate(f'{(height/total_control)*100:.2f}%', 
                                (p.get_x() + p.get_width() / 2., height), 
                                ha='center', va='bottom')

    plt.suptitle('Comparison of Categorical Variable Distributions between Campaign and Control Groups', size=20, y=1)
    plt.tight_layout()
    plt.show()

    return None

def compare_target_distributions(
    campaign_group: pd.DataFrame,
    control_group: pd.DataFrame,
    categorical_cols: list,
    target_col: str = 'y') -> None:

    categorical_cols_temp = [col for col in categorical_cols if col != target_col]

    num_cols = 2
    num_rows = len(categorical_cols_temp)

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 30))

    for i, category in enumerate(categorical_cols_temp):
        campaign_distribution = campaign_group.groupby(category)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)
        campaign_distribution = campaign_distribution.sort_values(by='yes', ascending=False)
        
        control_distribution = control_group.groupby(category)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)
        control_distribution = control_distribution.sort_values(by='yes', ascending=False)
        
        ax_campaign = campaign_distribution.plot(kind='bar', stacked=True, ax=axes[i, 0])
        ax_campaign.set_title(f"Campaign Group - Distribution of target in '{category}'")
        ax_campaign.set_xlabel(category)
        ax_campaign.set_ylabel('Percentage')
        ax_campaign.legend().remove()
        ax_campaign.tick_params(axis='x', rotation=45)
        
        for p in ax_campaign.patches:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy()
            if height > 0:
                ax_campaign.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

        ax_control = control_distribution.plot(kind='bar', stacked=True, ax=axes[i, 1])
        ax_control.set_title(f"Control Group - Distribution of target in '{category}'")
        ax_control.set_xlabel(category)
        ax_control.set_ylabel('Percentage')
        ax_control.legend().remove()
        ax_control.tick_params(axis='x', rotation=45)
        
        for p in ax_control.patches:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy()
            if height > 0:
                ax_control.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    handles, labels = ax_campaign.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', shadow=True, prop={'size': 14})

    plt.suptitle('Comparison of Target "y" Distribution Across Categorical Variables Between Campaign and Control Groups', size=20, y=1)
    plt.tight_layout()
    plt.show()

    return None

def compare_numeric_distributions(
    campaign_group: pd.DataFrame,
    control_group: pd.DataFrame,
    numeric_cols: list,
    target_col: str = 'y') -> None:

    num_cols = 2
    num_rows = len(numeric_cols)

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 30))

    for i, ax_row in enumerate(axes):
        sns.histplot(data=campaign_group, x=numeric_cols[i], hue=target_col, multiple='stack', ax=ax_row[0])
        ax_row[0].set_title(f"Campaign Group - Distribution of {numeric_cols[i]} by target variable")
        ax_row[0].set_xlabel(numeric_cols[i])
        ax_row[0].set_ylabel('Count')
        ax_row[0].tick_params(axis='x', rotation=45)

        sns.histplot(data=control_group, x=numeric_cols[i], hue=target_col, multiple='stack', ax=ax_row[1])
        ax_row[1].set_title(f"Control Group - Distribution of {numeric_cols[i]} by target variable")
        ax_row[1].set_xlabel(numeric_cols[i])
        ax_row[1].set_ylabel('Count')
        ax_row[1].tick_params(axis='x', rotation=45)

    plt.suptitle('Comparison of Numerical Variable Distribution Between Campaign and Control Groups by Target "y"', size=20, y=1)
    plt.tight_layout()
    plt.show()

    return None

def compare_boxplots(
    campaign_group: pd.DataFrame,
    control_group: pd.DataFrame,
    numeric_cols: list,
    target_col: str = 'y') -> None:

    num_cols = 2
    num_rows = len(numeric_cols)

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 20))

    for i, ax_row in enumerate(axes):
        sns.boxplot(data=campaign_group, x=target_col, y=numeric_cols[i], ax=ax_row[0])
        ax_row[0].set_title(f"Campaign Group - Boxplot of {numeric_cols[i]} by target variable")
        ax_row[0].set_xlabel('Target')
        ax_row[0].set_ylabel(numeric_cols[i])

        sns.boxplot(data=control_group, x=target_col, y=numeric_cols[i], ax=ax_row[1])
        ax_row[1].set_title(f"Control Group - Boxplot of {numeric_cols[i]} by target variable")
        ax_row[1].set_xlabel('Target')
        ax_row[1].set_ylabel(numeric_cols[i])

    plt.suptitle('Comparison of Boxplots Between Campaign and Control Groups by Target "y"', size=20, y=1)
    plt.tight_layout()
    plt.show()

    return None

def plot_stacked_bar(
    df: pd.DataFrame,
    category_col: str,
    target_col: str = 'y') -> None:

    category_distribution = df.groupby(category_col)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)

    ax = category_distribution.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(f'Stacked Barplot of {category_col.capitalize()} vs {target_col.upper()}', size=20)
    plt.xlabel(category_col.capitalize())
    plt.ylabel('Percentage')
    plt.legend(title=target_col.upper())
    plt.xticks(rotation=0)

    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        if height > 0:
            ax.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    plt.tight_layout() 
    plt.show()

    return None

def compare_stacked_bar(
    campaign_group: pd.DataFrame,
    control_group: pd.DataFrame,
    category_col: str,
    target_col: str = 'y') -> None:

    category_distribution_campaign = campaign_group.groupby(category_col)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)
    category_distribution_control = control_group.groupby(category_col)[target_col].value_counts(normalize=True).mul(100).unstack().fillna(0)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    ax_campaign = category_distribution_campaign.plot(kind='bar', stacked=True, ax=axes[0])
    ax_campaign.set_title(f"Campaign Group - Distribution of target by {category_col.capitalize()}")
    ax_campaign.set_xlabel(category_col.capitalize())
    ax_campaign.set_ylabel('Percentage')
    ax_campaign.legend(title=target_col.upper())
    ax_campaign.tick_params(axis='x', rotation=45)

    for p in ax_campaign.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        if height > 0:
            ax_campaign.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    ax_control = category_distribution_control.plot(kind='bar', stacked=True, ax=axes[1])
    ax_control.set_title(f"Control Group - Distribution of target by {category_col.capitalize()}")
    ax_control.set_xlabel(category_col.capitalize())
    ax_control.set_ylabel('Percentage')
    ax_control.legend(title=target_col.upper())
    ax_control.tick_params(axis='x', rotation=45)

    for p in ax_control.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        if height > 0:
            ax_control.annotate(f'{height:.2f}%', (x + width / 2, y + height / 2), ha='center', va='center')

    handles, labels = ax_campaign.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', shadow=True, prop={'size': 10})

    plt.suptitle(f'Comparison of Target "{target_col}" Distribution Across {category_col.capitalize()}', size=20, y=1.02)
    plt.tight_layout()
    plt.show()

    return None

def plot_numeric_boxplots(
    df: pd.DataFrame,
    numeric_cols: list,
    target_col: str = 'y',
    exclude_col: str = 'client_id') -> None:
    
    numeric_cols_temp = [col for col in numeric_cols if col != exclude_col]

    num_cols = 2
    num_rows = (len(numeric_cols_temp) + num_cols - 1) // num_cols

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(20, 20))

    for i, ax in zip(numeric_cols_temp, axes.flatten()):
        sns.boxplot(x=target_col, y=i, data=df, ax=ax)
        ax.set_title(f"Boxplot of {i} by target variable")
        ax.set_xlabel(f'Target ({target_col})')
        ax.set_ylabel(i)
        ax.tick_params(axis='x', rotation=45)

    plt.suptitle('Boxplots of Numeric Variables by Target "y"', size=20, y=1)
    plt.tight_layout()
    plt.show()
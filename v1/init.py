import pandas as pd

def init_excel():
    with pd.ExcelWriter('email_server.xlsx', engine='openpyxl', mode='w') as writer:
        users_df = pd.DataFrame(columns=['Username', 'EmailID', 'Password'])
        users_df.to_excel(writer, sheet_name='Users', index=False)

if __name__ == "__main__":
    init_excel()

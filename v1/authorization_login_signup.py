import pandas as pd

def signup(username, email, password):
    users_df = pd.read_excel('email_server.xlsx', sheet_name='Users')
    
    if username in users_df['Username'].values or email in users_df['EmailID'].values:
        return False, "Username or Email already exists."
    
    new_user = pd.DataFrame([[username, email, password]], columns=['Username', 'EmailID', 'Password'])
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    
    with pd.ExcelWriter('email_server.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        users_df.to_excel(writer, sheet_name='Users', index=False)
        pd.DataFrame(columns=['From', 'Contents', 'MailID', 'To', 'Contents', 'MailID']).to_excel(writer, sheet_name=username, index=False)
    
    return True, "Signup successful."

def login(email, password):
    users_df = pd.read_excel('email_server.xlsx', sheet_name='Users')
    user = users_df[(users_df['EmailID'] == email) & (users_df['Password'] == password)]
    
    if not user.empty:
        return True, user.iloc[0]['Username'], "Login successful."
    else:
        return False, None, "Invalid Email or Password."

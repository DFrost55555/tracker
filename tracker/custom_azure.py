from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'gmsadmstor01' # Must be replaced by your <storage_account_name>
    account_key = 'HbAbM+wVNKOjEjbeC6lFVILVkWao0Or/Ts5CICxNgOgoSsRWjoEpD91qowl8duaTkJ9H+qYqvAEmGkiVprzqfA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'gmsadmstor01' # Must be replaced by your storage_account_name
    account_key = 'HbAbM+wVNKOjEjbeC6lFVILVkWao0Or/Ts5CICxNgOgoSsRWjoEpD91qowl8duaTkJ9H+qYqvAEmGkiVprzqfA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
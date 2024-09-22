import os
auc_list = {}
def auc(auc_list):
        name=input("Enter the name of the bidder: ")
        amt=int(input("Enter the bidding amount: "))
        auc_list[name]=amt

end=False
while(not end):
    choice = input("Enter 'yes' if there are bidders: ")
    if choice=='yes':
        auc(auc_list)
        os.system('cls')
    else:
        end=True
        break
win=''
max=0
for i,j in auc_list.items():
    if(j>max):
        max=j
        win+=i
print(f"{win} wins with highest bid of {max}")


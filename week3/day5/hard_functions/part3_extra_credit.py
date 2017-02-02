#part 1
def taxes(tax_info,income):
    total = 0
    for i in range(len(tax_info)):
        if tax_info[i][0] < income:
            total += tax_info[i][0] * tax_info[i][1]
        else:
            total += (income - tax_info[i-1][0]) * tax_info[i][1]
            break
    total = '${:,.2f}'.format(total)
    return "You owe {0} in taxes.".format(total)

#part 2
def taxes2(tax_info,income):
    tax_info = sorted(tax_info)
    total = 0
    for i in range(len(tax_info)):
        if tax_info[i][0] < income:
            total += tax_info[i][0] * tax_info[i][1]
        else:
            total += (income - tax_info[i-1][0]) * tax_info[i][1]
            break
    total = '${:,.2f}'.format(total)
    return "You owe {0} in taxes.".format(total)

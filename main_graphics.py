from graphics import Exports

data_exports = Exports.exports_all_states('data_comexstat.csv', product='soybeans')

# Question - 1
# Exports - Monthly
Exports.curves_monthly()
Exports.hist_monthly()

# Exports - Yearly
Exports.hist_yearly()

# Question - 2
# Mostly important product exported - last 5 years
Exports.mostly_important_products('data_comexstat.csv')

# Question - 3
# Main routes - corn
Exports.routes_corn('data_comexstat.csv', product='wheat')

# Question - 4
# Corn and sugar partners
Exports.corn_sugar_partners('data_comexstat.csv')

# Question - 5
# Mostly important states
Exports.mostly_important_states('data_comexstat.csv', product='wheat')
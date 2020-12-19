from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import datetime


class Exports:
    
    @classmethod
    def exports_all_states(cls, path, product):
        
        # Loading data
        cls.__data = read_csv(path, encoding='ISO-8859-1')
        cls.__data = cls.__data[cls.__data['type'] == 'Export']
        
        if product == 'soybeans':
            cls.__data = cls.__data[cls.__data['product']=='soybeans']
        elif product == 'soybean_oil':
            cls.__data = cls.__data[cls.__data['product']=='soybean_oil']
        elif product == 'soybean_meal':
            cls.__data = cls.__data[cls.__data['product']=='soybean_meal']
        else:
            return None
        
        cls.__counter_exports()  # amount of exports
        
        return cls.__exports
    

    @classmethod
    def __counter_exports(cls):
        
        year = 1997
        month = 1
        cls.__exports = {'year': [], 'month': [], 'exports': []}  # All months
        counter = 0

        for i, d in enumerate(cls.__data['date']):
            date = datetime.datetime.strptime(d, '%Y-%m-%d')  # turning into datetime
            
            # Adding the quantity of exports
            if year == date.year:
                if month == date.month:
                    counter += 1
                else:
                    cls.__exports['year'].append(year)
                    cls.__exports['month'].append(month)
                    cls.__exports['exports'].append(counter)
                    month = date.month
                    counter = 1
            else:
                cls.__exports['year'].append(year)
                cls.__exports['month'].append(month)
                cls.__exports['exports'].append(counter)
                month = date.month
                year = date.year
                counter = 1
            
            # treatment for the last record
            if i == cls.__data.shape[0]-1:
                cls.__exports['year'].append(year)
                cls.__exports['month'].append(month)
                cls.__exports['exports'].append(counter)
                    
        cls.__exports = DataFrame(cls.__exports)
                    
    
    @classmethod
    def curves_monthly(cls):
        
        # curves every 5 years
        counter = 1
        for i in range(0, cls.__exports.shape[0], 12):
            plt.plot(range(1, 13), cls.__exports['exports'][i:i+12], label=str(cls.__exports['year'][i]))
            plt.xlabel('Months')
            plt.ylabel('Exports')
            plt.legend()
            
            if counter == 4:
                counter = 0
                plt.show()
            
            if i == 264:
                plt.show()
                
            counter += 1
    
    
    @classmethod
    def hist_monthly(cls):
        
        exports = []
        
        for month in range(1, 13):
            exports.append(cls.__exports[cls.__exports['month']==month].exports.sum())
        
        plt.bar(range(1, 13), exports)
        plt.xlabel('Month')
        plt.ylabel('Exports')
        plt.show()
        
        
    @classmethod
    def hist_yearly(cls):
        
        years = []
        exports = []
        
        for i in range(0, cls.__exports.shape[0], 12):
            year = cls.__exports['year'][i]
            
            years.append(year)
            exports.append(cls.__exports[cls.__exports['year']==year].exports.sum())  # number of exports
        
        plt.bar(years, exports)
        plt.xlabel('Year')
        plt.ylabel('Exports')
        plt.show()
    
    
    @classmethod
    def mostly_important_products(cls, path):
        
        # Loading data
        data = read_csv(path, encoding='ISO-8859-1')
        
        ind = 0
        
        for i, d in enumerate(data['date']):
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            if date.year >= 2015:
                ind = i
                break
        
        data = data.iloc[ind:]
        data = data[data['type'] == 'Export']
        
        data = data['product'].value_counts()
        
        plt.bar(data.keys()[0:3], data[0:3])
        plt.xlabel('Product')
        plt.ylabel('Exports')
        plt.show()
        
    
    @classmethod
    def routes_corn(cls, path, product):
        
        # Loading data
        data = read_csv(path, encoding='ISO-8859-1')
        data = data[data['product'] == product]
        
        # Last 4 years
        ind = 0
        
        for i, d in enumerate(data['date']):
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            if date.year >= 2016:
                ind = i
                break
        
        data = data.iloc[ind:]
        data = data[data['type'] == 'Export']
        
        data = data['route'].value_counts()
        
        plt.pie(data, labels=data.keys(), autopct='%1.1f%%')
        plt.title(product.title())
        plt.show()
    
    @classmethod
    def corn_sugar_partners(cls, path):
        
        # Loading data
        data = read_csv(path, encoding='ISO-8859-1')
        
        # Last 3 years
        ind = 0
        
        for i, d in enumerate(data['date']):
            date = datetime.datetime.strptime(d, '%Y-%m-%d')
            if date.year >= 2017:
                ind = i
                break
        
        data = data.iloc[ind:]
        data_corn = data[data['product']=='corn']
        data_sugar = data[data['product']=='sugar']
        
        data_corn = data_corn['country'].value_counts()
        data_sugar = data_sugar['country'].value_counts()
        
        plt.pie(data_corn[0:4], labels=data_corn.keys()[0:4], autopct='%1.1f%%')
        plt.title('Corn')
        plt.show()
        
        plt.pie(data_sugar[0:4], labels=data_sugar.keys()[0:4], autopct='%1.1f%%')
        plt.title('Sugar')
        plt.show()
    
    
    @classmethod
    def mostly_important_states(cls, path, product):
        
        # Loading data
        data = read_csv(path, encoding='ISO-8859-1')
        data = data[data['type'] == 'Export']
        data = data[data['product'] == product]
        
        data = data['state'].value_counts()
        
        plt.pie(data[0:5], labels=data.keys()[0:5], autopct='%1.1f%%')
        plt.title(product.title())
        plt.show()
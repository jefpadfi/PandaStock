from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import AccordionItem
from kivy.uix.button import Button
from kivy.uix.label import Label
from database import check_database_exists, create_connection, close_connection, create_database, get_portfolio_names, get_stock_names

Builder.load_file('main.kv')


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Check if the database file exits
        if check_database_exists("panda_stocks.db"):
            print("Database file exists.")
        else:
            print("Database file does not exist.")
            create_database("panda_stocks.db")
        
        # Load portfolio names from the database
        portfolios = self.load_portfolio_names()
        
        # Load stocks from the database
        stocks = self.load_stocks()
        
        # Create the accordion menu
        accordion = self.ids.portfolios
        
        if portfolios:
            for portfolio_name in portfolios:
                item = AccordionItem(title=portfolio_name[1])
                accordion.add_widget(item)
                
                # We need a box layout to have the items show up correctly.
                layout = BoxLayout(orientation='vertical')
                
                for stock in stocks:
                    if stock[2] == portfolio_name[0]:
                        stock_info = Button(text=stock[1], on_release=lambda btn, id=stock[0]: self.load_stock_info(id))
                        layout.add_widget(stock_info)
                
                item.add_widget(layout)
        else:
            item = AccordionItem(title="No Portfolios found")
            accordion.add_widget(item)
            add_portfolio_btn = Button(text="Add Portfolio")
            item.add_widget(add_portfolio_btn)
        
    def load_portfolio_names(self):
        # Create a connection to the database
        conn = create_connection("panda_stocks.db")
        
        # Retrieve portfolio names
        portfolio_names = get_portfolio_names(conn)
        
        # Close the database connection
        close_connection(conn)
        
        return portfolio_names
    
    def load_stocks(self):
        # Create a connection to the database
        conn = create_connection("panda_stocks.db")
        
        # Retrieve portfolio names
        stock_names = get_stock_names(conn)
        
        # Close the database connection
        close_connection(conn)
        
        return stock_names
    
    def load_portfolio_data(self, selected_portfolio):
        # Update Top right area with selected Portfolio
        self.ids.topLBL.text = "Selected Portfolio: {0}".format(selected_portfolio)
        
        # Update bottom right area with portfolio details
        self.ids.btmLBL.text = "Details for {0}".format(selected_portfolio)
    
    def load_stock_info(self, stock_id):
        # Update Top right area with selected Portfolio
        self.ids.topLBL.text = "Selected Stock: {0}".format(stock_id)
        
        # Update bottom right area with portfolio details
        self.ids.btmLBL.text = "Details for {0}".format(stock_id)


class PandaStock(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':        
    PandaStock().run()

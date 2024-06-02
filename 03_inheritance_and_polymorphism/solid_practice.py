class UserData:
    def __init__(self, name, email):
        self.name=name
        self.email=email
    
    def change_email(self,new_email):
        self.email=new_email
    
class UserProfileDisplay:
    
    @staticmethod
    def display_profile(name, email):
        return f"Name: {name}, Email: {email}"
    
class EmailNotifier:
    def send_email_change_notification(self, old_email, new_email):
        pass

user = UserData(name="John Doe", email="johndoe@example.com")

profile_info = UserProfileDisplay.display_profile(name=user.name, email=user.email)
print(profile_info)    


class BlogManager:
    def __init__(self):
        self.posts = []

    def create_post(self, title, content):
        self.posts.append({'title': title, 'content': content})

    
class BlogSave:
    def save_post_to_database(self, post):
        # 投稿をデータベースに保存するコード
        pass

class BlogRender:
    @staticmethod
    def render_post_in_html(self, post):
        return f"<h1>{post['title']}</h1><p>{post['content']}</p>"

# 割引の抽象クラス
class DiscountStrategy:
    def apply(self, order):
        raise NotImplementedError("Discount strategy must implement apply method.")

# 割引の具象クラス
class HolidayDiscount(DiscountStrategy):
    def apply(self, order):
        return order.total * 0.9  # 10%の割引

class VIPDiscount(DiscountStrategy):
    def apply(self, order):
        return order.total * 0.8  # 20%の割引

class BulkOrderDiscount(DiscountStrategy):
    def apply(self, order):
         if order.item_count >=10:
             return order.total * 0.85
         else:
             return order.total

class FirstTimeBuyerDiscount(DiscountStrategy):
    def apply(self, order):
        if order.is_first_time_buyer == "True":
            return order.total * 0.88
        else:
            return order.total

# 注文割引クラス
class OrderDiscount:
    def apply_discount(self, order, discount_strategy=None):
        if discount_strategy is None:
            discount_strategy = DefaultDiscount()
        return discount_strategy.apply(order)

# デフォルトの割引
class DefaultDiscount(DiscountStrategy):
    def apply(self, order):
        # デフォルトの割引ロジック (ある場合)、または単に注文合計を返す
        return order.total   
    
class Order:
    def __init__(self, total, item_count, is_first_time_buyer):
        self.total=total
        self.item_count=item_count
        self.is_first_time_buyer=is_first_time_buyer
    
# サンプルの注文インスタンス
order_bulk = Order(total=1000, item_count=11, is_first_time_buyer=False)
order_first_time = Order(total=800, item_count=5, is_first_time_buyer=True)

# 大量注文割引を適用
discount_calculator = OrderDiscount()
bulk_discount = BulkOrderDiscount()
final_price_bulk = discount_calculator.apply_discount(order_bulk, bulk_discount)

# 初回購入者割引を適用
first_time_discount = FirstTimeBuyerDiscount()
final_price_first_time = discount_calculator.apply_discount(order_first_time, first_time_discount)

print(f"Final price with bulk discount: {final_price_bulk}")
print(f"Final price for first-time buyer: {final_price_first_time}")



class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

class RefundablePaymentProcessor(PaymentProcessor):
    def process_refund(self, amount):
        raise NotImplementedError

class CreditCardPayment(RefundablePaymentProcessor):
    def process_payment(self, amount):
        # クレジットカードの支払いの処理
        pass

    def process_refund(self, amount):
        # クレジットカードの返金の処理
        pass

class BitcoinPayment(PaymentProcessor):
    def process_payment(self, amount):
        # ビットコインの支払いの処理
        pass

class WireTransferPayment(PaymentProcessor):
    def process_payment(self, amount):
        pass
    
class Printer:
    def print_document(self):
        raise NotImplementedError

class Scanner:
    def scan_document(self):
        raise NotImplementedError

class FaxMachine:
    def fax_document(self):
        raise NotImplementedError

# 実装
class AdvancedPrinter(Printer, Scanner, FaxMachine):
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass

class BasicPrinter(Printer):
    def print_document(self):
        pass

class Photocopier:
    def photocopy_document(self):
        raise NotImplementedError

class MultifunctionalDevice(Printer, Scanner, FaxMachine,Photocopier):
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass
    
    def photocopy_document(self):
        pass
    
class Database:
    def save_report(self, report):
        raise NotImplementedError

class MySQLDatabase(Database):
    def save_report(self, report):
        # MySQLデータベースへの保存を実装
        pass
    
class PostgreSQLDatabase(Database):
    def save_report(self, report):
        # MySQLデータベースへの保存を実装
        pass

class ReportGenerator:
    def __init__(self, database: Database):
        self.database = database

    def generate_report(self, report_data):
        report = self.create_report(report_data)
        self.database.save_report(report)

    def create_report(self, data):
        # レポートの作成ロジック
        pass
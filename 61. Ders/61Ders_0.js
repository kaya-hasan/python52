// singleton sınıflandırma

class DatabaseConnection {
  constructor() {
    if (DatabaseConnection.instance) {
      return DatabaseConnection.instance;
    }
    this.connection = null;
    this.connected = false;

    DatabaseConnection.instance = this;
  }
  connect(connectionString) {
    if (!this.connected) {
      this.connection = connectionString;
      this.connected = true;
      console.log("Veritabanı ile bağlantı sağlandı", connectionString);
    } else {
      console.log("Bağlantı zaten kurulu");
    }
  }
  disconnect() {
    this.connection = null;
    this.connected = false;
    console.log("Bağlantı kesildi");
  }
  getStatus() {
    return this.connected ? "Bağlantı aktif" : "Bağlantı yok";
  }
}

const db1 = new DatabaseConnection();
db1.connect("....");

const db2 = new DatabaseConnection();
db2.connect("....");

console.log(db1 === db2); // true
console.log(db1.getStatus());

// observer pattern
class NewsAgency {
  constructor() {
    this.subscribers = [];
    this.latesNews = null;
  }
  subscribe(observer) {
    this.subscribers.push(observer);
    console.log(`${observer.name} haberlere abone oldu`);
  }
  unsubscribe(observer) {
    this.subscribers = this.subscribers.filter((sub) => sub !== observer);
    console.log(`${observer.name} abonelikten çıktı`);
  }
  notifyAll() {
    console.log("----- Tüm aboneler için bilgilendirme -----");
    this.subscribers.forEach((subscriber) => {
      subscriber.update(this.latesNews);
    });
  }
  publishNews(news) {
    console.log(`Yeni haber ------ ${news} -------`);
    this.latesNews = news;
    this.notifyAll();
  }
}

class NewsSubscriber {
  constructor(name) {
    this.name = name;
  }
  update(news) {
    logger(`${this.name} haberi almıştır: ${news}`);
  }
}

const agency = new NewsAgency();
const emre = new Subscriber("Emre");
const batuhan = new Subscriber("Batuhan");
const hasan = new Subscriber("Hasan");

agency.subscribe(emre);
agency.subscribe(batuhan);
agency.subscribe(hasan);

agency.publishNews("Örnek bir haber yayınlandı");

agency.unsubscribe(emre);

agency.publishNews("Örnek haber 2");

// module

// module pattern - IIFE (Immediately Invoked Function Expression) kullanarak bir modül oluşturma tekniğidir. Bu desen, değişkenlerin ve fonksiyonların kapsül içinde saklanmasını sağlar ve sadece belirli bir arayüzü dışarıya açar. Bu sayede, modülün içindeki değişkenler ve fonksiyonlar global alanda görünmez hale gelir ve çakışmaların önüne geçilir. Modül deseni, JavaScript'te kod organizasyonu ve yeniden kullanılabilirlik için yaygın olarak kullanılır.
const ShoppingCart = (function () {
  let items = [];
  function addItem(item) {
    items.push(item);
    console.log(`${item} sepete eklendi`);
  }
  function removeItem(item) {
    items = items.filter((i) => i !== item);
    console.log(`${item} sepetten çıkarıldı`);
  }
  function getItems() {
    return items;
  }
  return {
    addItem,
    removeItem,
    getItems,
  };
})();

ShoppingCart.addItem("Elma");
ShoppingCart.addItem("Armut");
console.log(ShoppingCart.getItems());

// mediator pattern = Mediator deseni, nesneler arasındaki iletişimi merkezi bir aracı (mediator) üzerinden yönetmeyi amaçlayan bir tasarım desenidir. Bu desen, nesneler arasındaki doğrudan iletişimi azaltarak, bağımlılıkları azaltır ve kodun daha esnek ve bakımı kolay hale gelmesini sağlar. Mediator, nesneler arasındaki etkileşimleri kontrol eder ve koordinasyonu sağlar, böylece nesneler birbirleriyle doğrudan iletişim kurmak zorunda kalmazlar. Bu desen, özellikle karmaşık sistemlerde nesneler arasındaki ilişkilerin yönetilmesi gerektiğinde kullanışlıdır.
// ana mediator tanımlanır ve bunun üzerinden diğer objeler iletişim kurar
class ChatRoom {
  constructor() {
    this.users = [];
  }
  addUser(user) {
    this.users.push(user);
  }
  sendMessage(message, sender) {
    this.users.forEach((user) => {
      if (user !== sender) {
        user.receiveMessage(message, sender);
      }
    });
  }
}

class User {
  constructor(name, chatRoom) {
    this.name = name;
    this.chatRoom = chatRoom;
    this.chatRoom.addUser(this);
  }
  sendMessage(message, sender) {
    console.log(`${this.name} ${sender.name}den mesaj aldı: ${message}`);
  }
}

const chatRoom = new ChatRoom();
const user1 = new User("Ahmet", chatRoom);
const user2 = new User("Mehmet", chatRoom);

user1.sendMessage("Merhaba", user2);

// factory
// factory deseni, nesne oluşturma sürecini merkezi bir noktaya taşıyan bir tasarım desenidir. Bu desen, nesnelerin nasıl oluşturulacağını ve hangi sınıfların kullanılacağını belirlemek için bir arayüz sağlar. Factory deseni, nesne oluşturma sürecini soyutlayarak, kodun daha esnek ve genişletilebilir olmasını sağlar. Bu desen, özellikle nesne oluşturma sürecinin karmaşık olduğu durumlarda veya farklı türde nesnelerin oluşturulması gerektiğinde kullanışlıdır.
class Car {
  constructor(brand, model) {
    this.brand = brand;
    this.model = model;
  }
}

class CarFactory {
  createCar(brand, model) {
    return new Car(brand, model);
  }
}

const factory = new CarFactory();
const car1 = factory.createCar("Toyota", "Corolla");
const car2 = factory.createCar("Honda", "Civic");

console.log(car1);
console.log(car2);

// decarotor pattern = Decorator deseni, bir nesnenin davranışını dinamik olarak değiştirmek veya genişletmek için kullanılan bir tasarım desenidir. Bu desen, nesneleri sarmalayarak (wrap) yeni özellikler eklemeye veya mevcut özellikleri değiştirmeye olanak tanır. Decorator deseni, özellikle nesnelerin davranışlarını değiştirmek istediğiniz durumlarda veya farklı kombinasyonlarda özellikler eklemek istediğinizde kullanışlıdır. Bu desen, nesnelerin birbirlerine bağımlılığını azaltır ve kodun daha esnek ve genişletilebilir olmasını sağlar.
class Coffee {
  cost() {
    return 10;
  }
  description() {
    return "Kahve";
  }
}

class MilkDecorator {
  constructor(coffee) {
    this.coffee = coffee;
  }
  cost() {
    return this.coffee.cost() + 2;
  }
  description() {
    return this.coffee.description() + ", Süt";
  }
}

class SugarDecorator {
  constructor(coffee) {
    this.coffee = coffee;
  }
  cost() {
    return this.coffee.cost() + 1;
  }
  description() {
    return this.coffee.description() + ", Şeker";
  }
}

const coffee = new Coffee();
const coffeeWithMilk = new MilkDecorator(coffee);
const coffeeWithMilkAndSugar = new SugarDecorator(coffeeWithMilk);

console.log(coffee.cost());
console.log(coffeeWithMilk.cost());
console.log(coffeeWithMilkAndSugar.cost());

console.log(coffee.description());
console.log(coffeeWithMilk.description());
console.log(coffeeWithMilkAndSugar.description());

// strategy pattern = Strategy deseni, bir algoritmanın veya davranışın farklı varyasyonlarını tanımlamak ve bu varyasyonları birbirinin yerine kullanmak için kullanılan bir tasarım desenidir. Bu desen, algoritmaların veya davranışların birbirinden bağımsız olarak değiştirilebilmesini sağlar ve kodun daha esnek ve genişletilebilir olmasını sağlar. Strategy deseni, özellikle bir işlemi gerçekleştirmek için birden fazla algoritma veya davranış seçeneği olduğunda kullanışlıdır.
class PaymentStrategy {
  pay(amount) {
    throw new Error("pay() metodu implement edilmeli");
  }
}

class CreditCardStrategy extends PaymentStrategy {
  pay(amount) {
    console.log(`${amount} TL kredi kartı ile ödendi`);
  }
}

class PaypalStrategy extends PaymentStrategy {
  pay(amount) {
    console.log(`${amount} TL PayPal ile ödendi`);
  }
}

class ShoppingCart {
  constructor() {
    this.items = [];
    this.paymentStrategy = null;
  }
  setPaymentStrategy(paymentStrategy) {
    this.paymentStrategy = paymentStrategy;
  }
  addItem(item) {
    this.items.push(item);
  }
  checkout() {
    const total = this.items.reduce((sum, item) => sum + item.price, 0);
    this.paymentStrategy.pay(total);
  }
}

const cart = new ShoppingCart();
cart.addItem({ name: "Elma", price: 10 });
cart.addItem({ name: "Armut", price: 20 });

cart.setPaymentStrategy(new CreditCardStrategy());
cart.checkout();

cart.setPaymentStrategy(new PaypalStrategy());
cart.checkout();

// proxy pattern
// proxy pattern bir nesnenin yerine geçen bir nesne oluşturarak, gerçek nesneye erişimi kontrol etmek veya ek işlevsellik sağlamak için kullanılan bir tasarım desenidir. Proxy deseni, gerçek nesnenin oluşturulması veya erişilmesi maliyetli olduğunda veya güvenlik, önbellekleme gibi ek özellikler gerektiğinde kullanışlıdır. Proxy, gerçek nesneye erişimi kontrol eder ve gerektiğinde gerçek nesneyi oluşturur veya işlemleri yönlendirir.
class RealImage {
  constructor(filename) {
    this.filename = filename;
    this.loadFromDisk();
  }
  loadFromDisk() {
    console.log(`Resim yükleniyor: ${this.filename}`);
  }
  display() {
    console.log(`Resim gösteriliyor: ${this.filename}`);
  }
}

class ImageProxy {
  constructor(filename) {
    this.filename = filename;
    this.realImage = null;
  }
  display() {
    if (!this.realImage) {
      this.realImage = new RealImage(this.filename);
    }
    this.realImage.display();
  }
}

const image = new ImageProxy("resim.jpg");
image.display(); // fotoğraf yüklemesi yapılmış

// facade pattern
// facade pattern bir alt sistemin karmaşıklığını gizleyerek, daha basit bir arayüz sağlayan bir tasarım desenidir. Bu desen, alt sistemin karmaşıklığını kullanıcıdan saklar ve sadece gerekli olan işlevselliği sunar. Facade deseni, özellikle karmaşık sistemlerde kullanıcıların alt sistemi doğrudan kullanmak yerine, daha basit bir arayüz üzerinden etkileşimde bulunmalarını sağlamak için kullanışlıdır.
class Facade {
  operationA() {
    console.log("İşlem A");
  }
  operationB() {
    console.log("İşlem B");
  }
  operationC() {
    console.log("İşlem C");
  }
  executeAll() {
    this.operationA();
    this.operationB();
    this.operationC();
  }
}

const facade = new Facade();
facade.executeAll();

// solid
// S — Single-responsibility principle
// O — Open-closed principle
// L — Liskov substitution principle
// I — Interface segregation principle
// D — Dependency inversion principle

// S - Sorumluluk - Her class bir işten sorumludur
class UserAuth {
  constructor(user) {
    this.user = user;
  }

  authenticate(password) {
    // Sadece kimlik doğrulama ile ilgilenir
    return this.user.password === password;
  }
}

class Logger {
  logError(error) {
    // Sadece loglama ile ilgilenir
    console.error(error);
  }
}

// open close
class PaymentProcessor {
  process(paymentMethod) {
    paymentMethod.pay();
  }
}

class CreditCardPayment {
  pay() {
    console.log("Kredi kartı ile ödendi.");
  }
}

class CryptoPayment {
  pay() {
    console.log("Kripto ile ödendi.");
  }
}

// Yeni bir ödeme yöntemi geldiğinde PaymentProcessor'a dokunmuyoruz.

// Liskov substitution - Bir sınıfın alt sınıfları, üst sınıfın yerine geçebilir ve aynı şekilde çalışmalıdır. Yani, bir alt sınıf, üst sınıfın beklenen davranışını değiştirmemelidir.
// Liskov - Yerine Geçme
class Bird {
  eat() {
    console.log("Yemek yiyor...");
  }
}

class FlyingBird extends Bird {
  fly() {
    console.log("Uçuyor...");
  }
}

class Duck extends FlyingBird {} // Ördek uçabilir
class Penguin extends Bird {} // Penguen sadece yer, fly() metoduna sahip değildir.

// I --- Arayüz
// Herkesin her şeyi yapabildiği dev bir "Worker" sınıfı yerine:
const opener = {
  openDoor() {
    console.log("Kapı açıldı.");
  },
};

const closer = {
  closeDoor() {
    console.log("Kapı kapandı.");
  },
};

const alarmSetter = {
  setAlarm() {
    console.log("Alarm kuruldu.");
  },
};

// Sadece kapı görevlisi için gerekenler:
const doorPerson = Object.assign({}, opener, closer);

// D - Bağımlılık
class Store {
  constructor(paymentProcessor) {
    // Store, belirli bir ödeme yöntemine (örn: PayPal) değil,
    // genel bir işlemciye bağımlıdır.
    this.paymentProcessor = paymentProcessor;
  }

  purchase(amount) {
    this.paymentProcessor.pay(amount);
  }
}

class StripeProcessor {
  pay(amount) {
    console.log(`Stripe ile ${amount} ödeme yapıldı.`);
  }
}

// Kullanım
const store = new Store(new StripeProcessor());
store.purchase(100);

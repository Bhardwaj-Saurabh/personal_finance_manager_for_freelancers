# Reflection

## Design Patterns Used

### 1. Singleton Pattern (Balance class)

The Balance class uses the Singleton pattern so there is only one instance managing the balance across the entire app. This makes sense because in a finance app, you never want two separate balance objects getting out of sync. The `get_instance()` method handles creating and returning the single instance. Direct instantiation raises an error to prevent accidental misuse.

### 2. Adapter Pattern (TransactionAdapter class)

The Adapter pattern converts external freelance income data into the app's internal Transaction format. The ExternalFreelanceIncome class has fields like invoice_id and description that the app doesn't need. The TransactionAdapter strips that away and creates a clean Transaction object. This keeps the core app decoupled from third-party data formats. If a new external platform shows up with a different structure, we just write a new adapter.

### 3. Observer Pattern (PrintObserver, LowBalanceAlertObserver)

The Observer pattern lets the Balance notify registered observers whenever a transaction is applied. PrintObserver logs every balance change. LowBalanceAlertObserver triggers an alert when the balance drops below a threshold. The Balance class doesn't need to know what the observers do. It just calls `update()` on each one. This makes it easy to add new observers like email alerts or logging without touching the Balance code.

### 4. Strategy Pattern (TaxStrategy, DiscountStrategy)

I chose the Strategy pattern because financial apps often need to process amounts differently depending on context. A freelance expense might have tax added, or a bulk purchase might get a discount. Instead of hardcoding these rules into the Balance class, each processing rule is its own strategy class with an `apply(amount)` method. The `apply_transaction()` method accepts an optional strategy, keeping it fully backward compatible.

I picked this over other patterns because it solves a real problem in finance apps. Tax rules change, discount structures vary by client, and you don't want to rewrite core logic every time. Strategy keeps that flexible.

## Trade-offs

The Singleton pattern makes unit testing harder because state carries over between tests. We handle this with a `reset()` method, but it means every test has to remember to call it. In a larger app, dependency injection would be a cleaner approach.

The Observer pattern adds a layer of indirection. When debugging, you have to trace through the observer list to understand what happens after a transaction. For a small app like this, it's manageable. In a bigger system, an event bus might be more appropriate.

The Strategy pattern adds extra classes for what could be simple math. For this app, three strategy classes might feel like overkill. But the pattern pays off as soon as you need more than two or three processing rules, which is common in real finance apps.

Overall, the patterns make the code more modular and testable, even if they add some complexity. Each component can be developed, tested, and modified independently, which is the whole point.

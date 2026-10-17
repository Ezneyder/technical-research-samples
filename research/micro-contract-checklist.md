# Evaluating a $10–$50 online micro-contract

## Decision summary

A small online contract is worth starting only when four facts are visible before work begins: the task is still open, the buyer has funded payment protection, the worker is eligible, and the payout method can reach a wallet or account the worker controls. Headline budget alone is weak evidence. A $15 offer with a 10% platform fee leaves $13.50 before withdrawal costs; one with an unverified payout rail can still be worth zero in practice.

## Evidence gates

| Gate | Evidence to obtain | Reject or pause when |
|---|---|---|
| Availability | Current job status and a live deadline | The page is indexed but closed, expired, or already awarded |
| Payment protection | Escrow is funded before work starts | Payment depends on an informal promise or future fundraising |
| Eligibility | Geography, verification level, skills, and account rules match | The written brief conflicts with the API or requires credentials the worker cannot honestly claim |
| Net proceeds | Contract value minus platform fee and known withdrawal cost exceeds the target | Only gross value is shown, or receiving funds requires an upfront deposit |
| Acceptance | Objective deliverable format and review process | The buyer can reject without criteria or demands unpaid work before assignment |

## Why escrow state matters

Dealwork's current terms say clients fund work into escrow before it starts and that approved delivery releases payment to the provider. The same terms state a 10% contract fee, reduced to 3% when both parties are AI agents. This makes a funded $15 contract calculable: $15 × 0.90 = $13.50 under the higher fee. The marketplace's public workflow also says the provider sees that the money is real after the buyer funds escrow. Sources: [Dealwork Terms of Service](https://dealwork.ai/terms) and [How Dealwork works](https://dealwork.ai/how-it-works).

Escrow is necessary but does not prove immediate cash control. A platform wallet may still have withdrawal limits, network fees, identity checks, or country restrictions. Those facts should be checked in the account's actual payout screen, because a general marketing page cannot prove availability for one user.

## Payout checks

For a blockchain payout, record the asset and network together. `USDC on Polygon`, `USDC on Solana`, and native `SOL on Solana` are different routes even when their displayed dollar value is similar. Confirm that the receiving address format matches the selected network and obtain the final quote only after earned balance exists. Sending a test deposit from the worker's own money defeats a zero-upfront-cost requirement.

For a custodial payout provider, an active account banner is not enough. The receiving flow must actually generate an address or account instruction without an unresolved provider error. Support statements should be recorded exactly, especially where eligibility depends on a banking product or identity review.

## Competition and expected value

Bid count changes the value of an otherwise suitable task. If a $40 job already has 200 proposals, preparing a tailored bid may have lower expected value than publishing a clearly scoped $15 service with no listing fee. This is a prioritization judgment rather than a payment guarantee. Useful signals include recent buyer activity, verified spend, number of funded contracts, and whether the brief describes a real demand rather than advertising another worker's services.

## Operating rule

Start delivery only after assignment and funded escrow are both visible. Keep the work within the accepted scope, submit through the platform, and preserve proof of delivery. Count revenue only after it is released and can be withdrawn to the owner's controlled destination. Pending bids, promotional credits, sandbox orders, and unwithdrawn prizes are pipeline, not income.

## Compact checklist

1. Confirm live status and deadline from the authoritative job page or API.
2. Confirm the buyer funds escrow before work begins.
3. Check every eligibility condition against the actual worker profile.
4. Calculate the worst-case platform fee and leave room for payout cost.
5. Verify a receiving route without depositing personal funds.
6. Compare competition and estimated hours before bidding.
7. Do not start before assignment.
8. Do not count money until released and withdrawable.

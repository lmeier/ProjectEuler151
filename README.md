# ProjectEuler151

My solution to [problem 151 of Project Euler](https://projecteuler.net/problem=151).

In this problem, there's a print shop, that starts with A1 paper, and successively halves paper in order to get A5 sheets. The foreman of the shop reaches into an envelope containing the papers whenever he needs a new A5 sheet, and will go through the halving process until he has an A5 piece. E.g. he reaches in and grabs and A3 sheet, he halves that into two A4s, and halves one of the A4s into an A5. All remaining pieces go back into the envelop.

The question is, how many times per A1 sheet can he expect to reach into the envelop and find only 1 sheet of paper? For the purposes here, we are excluding the first time he grabs paper (one large A1) and the 16th and last time, when there is certain to be just a single A5 sheet.

The very first solution that appeared to me was to just run a monte carlo simulatioun of the foreman reaching into the envelope. Though this is quite simple, the problem asks for 6 decimals of precision, making this non-optimal.

The next obvious solution is to traverse a tree of the possible paths, in proportion to how likely it is that that path obtains. This turns out to be very computationally demanding.

Dynamic programming, caching subsolutions, can be used to dramatically reduce the ammount of computation. This solves the problem in a fraction of a second on my MBP. I also coded up the MC simulation--through 100k iterations, it only achieves 3 decimal places of precision.

import rx
import rx.operators as ops

source = rx.from_iterable([1, 2, 3, 4])

source.pipe(
    ops.map(lambda i: i - 1),
    ops.filter(lambda i: i % 2 == 0),
).subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_completed=lambda: print("on_completed"),
    on_error=lambda e: print("on_error: {}".format(e))
)

def length_more_than_5():
    return rx.pipe(
        ops.map(lambda s: len(s)),
        ops.filter(lambda i: i >= 5),
    )

rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
    length_more_than_5()
).subscribe(lambda value: print("Received {0}".format(value)))

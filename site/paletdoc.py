from __future__ import annotations
from dataclasses import dataclass

@dataclass
class code:
    val: str

@dataclass
class var:
    val: str


@dataclass
class text:
    children: list[str | code]


@dataclass
class proc:
    name: str
    sig: tuple[list[str], str]
    argsig: list[tuple[str, str] | tuple[str, str, str]]
    summary: text


@dataclass
class syntax:
    name: str
    body: str
    summary: text


@dataclass
class value:
    name: str
    sig: str
    summary: text

doc: dict[str, list[proc | value | syntax | text]] = {
    "Basic Syntax": [
        syntax(
            "define",
            "id expr",
            text(["Set ", var("id"), " to the result of ", var("expr"), "."]),
        ),
        syntax(
            "set!",
            "id expr",
            text([
                "Set the result of ", var("expr"), " to ", var("id"), " if ",
                var("id"), " is already defined. If ", var("id"),
                " is not defined, raise an error.",
            ]),
        ),
    ],
    "Equality": [
        proc(
            "equal?",
            (["v1", "v2"], "boolean?"),
            [("v1", "any/c"), ("v2", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v1"), " and ", var("v2"),
                " are the same type and have the same value, ", code("#f"), " otherwise."
            ]),
        ),
    ],
    "Booleans": [
        proc(
            "boolean?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is ", code("#t"), " or ",
                code("#f"), ", ", code("#f"), " otherwise."
            ]),
        ),
        value("true", "boolean?", text(["An alias for ", code("#t"), "."])),
        value("false", "boolean?", text(["An alias for ", code("#f"), "."])),
        syntax(
            "if",
            "test-expr then-expr else-expr",
            text([
                "Evaluates ", var("test-expr"), ". If ", code("#t"), " then evaluate ",
                var("then-expr"), " else evaluate ", var("else-expr"),
                ". An error will be raised if evaluated ",
                var("test-expr"), " is not a ", code("boolean?"), ".",
            ]),
        ),
        syntax(
            "when",
            "test-expr body",
            text([
                "Evaluates ", var("test-expr"), ". If ", code("#t"), " then evaluate ",
                var("body"), " else do nothing. An error will be raised if evaluated ",
                var("test-expr"), " is not a ", code("boolean?"), ".",
            ]),
        ),
    ],
    "Number Predicates": [
        proc(
            "number?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is a number, ", code("#f"),
                " otherwise.",
            ]),
        ),
        proc(
            "real?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is a real number, ",
                code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "integer?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"),
                " is an integer or a number that can be coerced to an integer without changing value, ",
                code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "exact-integer?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is an integer and exact, ",
                code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "exact-nonnegative-integer?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is an exact integer and ",
                var("v"), " is greater than ", code("-1"), ", ", code("#f"),
                " otherwise.",
            ]),
        ),
        proc(
            "zero?",
            (["v"], "boolean?"),
            [("v", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is equal to ", code("0"),
                ", ", code("#f"), " otherwise."
            ]),
        ),
        proc(
            "positive?",
            (["v"], "boolean?"),
            [("v", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is greater than ",
                code("0"), ", ", code("#f"), " otherwise."
            ]),
        ),
        proc(
            "negative?",
            (["v"], "boolean?"),
            [("v", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is less than ", code("0"),
                ", ", code("#f"), " otherwise."
            ]),
        ),
    ],
    "Numbers": [
        proc(
            "+",
            (["z", "..."], "number?"),
            [("z", "number?")],
            text([
                "Return the sum of ", var("z"),
                "s. Add from left to right. If no arguments are provided, the result is ",
                code("0"), ".",
            ]),
        ),
        proc(
            "-",
            (["z", "w", "..."], "number?"),
            [("z", "number?"), ("w", "number?")],
            text([
                "When no ", var("w"), "s are applied, return ", code("(- 0 z)"),
                ". Otherwise, return the subtraction of ", var("w"), "s of ", var("z"),
                ".",
            ]),
        ),
        proc(
            "*",
            (["z", "..."], "number?"),
            [("z", "number?")],
            text([
                "Return the product of ", var("z"), "s. If no ", var("z"),
                "s are supplied, the result is ", code("1"), ".",
            ]),
        ),
        proc(
            "/",
            (["z", "w", "..."], "number?"),
            [("z", "number?"), ("w", "number?")],
            text([
                "When no ", var("w"), "s are applied, return ", code("(/ 1 z)"),
                ". Otherwise, return the division of ", var("w"), "s of ", var("z"),
                ".",
            ]),
        ),
        proc(
            "mod",
            (["n", "m"], "integer?"),
            [("n", "integer?"), ("m", "integer?")],
            text(["Return the modulo of ", var("n"), " and ", var("m"), "."]),
        ),
        proc(
            "modulo",
            (["n", "m"], "integer?"),
            [("n", "integer?"), ("m", "integer?")],
            text(["Clone of ", code("mod"), "."]),
        ),
        proc(
            "add1",
            (["z"], "number?"),
            [("z", "number?")],
            text(["Returns ", code("(+ z 1)"), "."]),
        ),
        proc("sub1",
            (["z"], "number?"),
            [("z", "number?")],
            text(["Returns ", code("(- z 1)"), "."]),
        ),
        proc(
            "=",
            (["z", "w", "..."], "boolean?"),
            [("z", "number?"), ("w", "number?")],
            text([
                "Returns ", code("#t"), " if all arguments are numerically equal, ",
                code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "<",
            (["x", "y"], "boolean?"),
            [("x", "real?"), ("y", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("x"), " is less than ", var("y"),
                ", ", code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "<=",
            (["x", "y"], "boolean?"),
            [("x", "real?"), ("y", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("x"), " is less than or equal to ",
                var("y"), ", ", code("#f"), " otherwise.",
            ]),
        ),
        proc(
            ">",
            (["x", "y"], "boolean?"),
            [("x", "real?"), ("y", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("x"), " is greater than ", code("y"),
                ", ", code("#f"), " otherwise.",
            ]),
        ),
        proc(
            ">=",
            (["x", "y"], "boolean?"),
            [("x", "real?"), ("y", "real?")],
            text([
                "Returns ", code("#t"), " if ", var("x"), " is greater than or equal to ",
                var("y"), ", ", code("#f"), " otherwise.",
            ]),
        ),
        proc(
            "abs",
            (["x"], "real?"),
            [("x", "real?")],
            text(["Returns the absolute value of ", var("x"), "."]),
        ),
        proc(
            "max",
            (["x", "..."], "real?"),
            [("x", "real?")],
            text(["Returns largest value of the ", var("x"), "s."]),
        ),
        proc(
            "min",
            (["x", "..."], "real?"),
            [("x", "real?")],
            text(["Returns smallest value of the ", var("x"), "s."]),
        ),
    ],
    "Vectors": [
        proc(
            "vector?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is a vector, ",
                code("#f"), " otherwise."
            ]),
        ),
        proc(
            "vector",
            (["v", "..."], "vector?"),
            [("v", "any/c")],
            text([
                "Returns a new vector with the ",
                var("v"), " args filled with its slots in order."
            ]),
        ),
        proc(
            "make-vector",
            (["size", "[v]"], "vector?"),
            [("size", "exact-nonnegative-integer"), ("v", "any/c", "0")],
            text([
                "Returns a new vector with ", var("size"),
                " slots, all filled with ", var("v"), "s."
            ]),
        ),
        proc(
            "vector-pop!",
            (["vec"], "any/c"),
            [("vec", "vector?")],
            text(["Remove the last element of ", var("vec"), " and return it."]),
        ),
        proc(
            "vector-add!",
            (["vec", "v"], "none"),
            [("vec", "vector?"), ("v", "any/c")],
            text(["Append ", var("v"), " to the end of ", var("vec"), "."]),
        ),
        proc(
            "vector-set!",
            (["vec", "pos", "v"], "none"),
            [("vec", "vector?"), ("pos", "exact-integer?"), ("v", "any/c")],
            text(["Set slot ", var("pos"), " of ", var("vec"), " to ", var("v"), "."]),
        ),
        proc(
            "vector-extend!",
            (["vec", "vec2", "..."], "none"),
            [("vec", "vector?"), ("vec2", "vector?")],
            text([
                "Append all elements of ", var("vec2"), " to the end of ",
                var("vec"), " in order.",
            ]),
        ),
    ],
    "Arrays": [
        proc(
            "array?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is an array, ", code("#f"),
                " otherwise."
            ]),
        ),
        proc(
            "array",
            (["dtype", "v", "..."], "array?"),
            [("dtype", "string?"), ("v", "any/c")],
            text([
                "Returns a freshly allocated array with ", var("dtype"), " as its ",
                "datatype and the ", var("v"), " args as its values filled in order."
            ]),
        ),

    ],
    "Pairs and Lists": [
        proc(
            "pair?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is a pair, ", code("#f"),
                " otherwise."
            ]),
        ),
        proc(
            "null?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"), " is an empty list, ", code("#f"),
                " otherwise."
            ]),
        ),
        proc(
            "cons",
            (["a", "d"], "pair?"),
            [("a", "any/c"), ("d", "any/c")],
            text([
                "Returns a newly allocated pair where ", var("a"),
                " is the first item and, ", var("d"), " is the second."
            ]),
        ),
        proc(
            "car",
            (["p"], "any/c?"),
            [("p", "pair?")],
            text([
                "Returns the first element of the pair ", var("p"), ".",
            ]),
        ),
        proc(
            "cdr",
            (["p"], "any/c?"),
            [("p", "pair?")],
            text([
                "Returns the second element of the pair ", var("p"), ".",
            ]),
        ),
        proc(
            "list?",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " if ", var("v"),
                " is an empty list or a pair whose second element is a list.",
            ]),
        ),
    ],
    "Generic Sequence "
    "Contracts": [
        proc(
            "any/c",
            (["v"], "boolean?"),
            [("v", "any/c")],
            text([
                "Returns ", code("#t"), " regardless of the value of ", var("v"), ".",
            ]),
        ),
    ],
}
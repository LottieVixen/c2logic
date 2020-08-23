binary_ops = {
	"+": "add",
	"-": "sub",
	"*": "mul",
	"/": "div",
	"%": "mod",
	"==": "equal",
	"!=": "notEqual",
	"<": "lessThan",
	"<=": "lessThanEq",
	">": "greaterThan",
	">=": "greaterThanEq",
	">>": "shl",
	"<<": "shr",
	"|": "or",
	"&": "and",
	"^": "xor"
}
condition_ops = {
	"==": "equal",
	"!=": "notEqual",
	"<": "lessThan",
	"<=": "lessThanEq",
	">": "greaterThan",
	">=": "greaterThanEq"
}

unary_ops = {"-": "negate", "~": "not"}

binary_op_inverses = {"==": "!=", "!=": "==", "<": ">=", "<=": ">", ">": "<=", ">=": "<"}

# roman-numeral-converter

Convert between integers and Roman numerals.

## Usage

```bash
python3 -c "from roman import *; print(to_roman(1994)); print(from_roman('MCMXCIV'))"
```

## Features

- Integer to Roman conversion for 1 to 3999
- Strict Roman parsing with validation
- Addition with add_roman(left, right)

## Tests

```bash
python3 -m unittest -q
```

## License

MIT

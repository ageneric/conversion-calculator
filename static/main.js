var items = [];

class AddStep extends React.Component {
  constructor(props) {
    super(props);
    this.state = { items: [], numericBase: 'dec', numericValue: '', calcType: '_bin' };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.addCalc = this.addCalc.bind(this);
    this.changeBase = this.changeBase.bind(this);
    this.changeValue = this.changeValue.bind(this);
    this.changeCalc = this.changeCalc.bind(this);
    this.clear = this.clear.bind(this);
  }


  render() {
    return React.createElement(
      "div",
      null,
      React.createElement(
        "div",
        { "class": "form" },
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "label",
            { "for": "data-type" },
            "Data Type"
          ),
          React.createElement(
            "select",
            { name: "data-type",
              onChange: this.changeBase,
              value: this.state.numericBase },
            React.createElement(
              "option",
              { value: "bin" },
              "Binary"
            ),
            React.createElement(
              "option",
              { value: "oct" },
              "Octal"
            ),
            React.createElement(
              "option",
              { value: "dec", selected: true },
              "Decimal"
            ),
            React.createElement(
              "option",
              { value: "hex" },
              "Hexadecimal"
            ),
            React.createElement(
              "option",
              { value: "bcd" },
              "BCD"
            )
          )
        ),
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "label",
            { "for": "data-value" },
            "Base 10 Value"
          ),
          React.createElement("input", { name: "data-value",
            onChange: this.changeValue,
            value: this.state.numericValue })
        ),
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "button",
            { type: "add-data", onClick: this.handleSubmit },
            "Add Number"
          )
        )
      ),
      React.createElement(
        "div",
        { "class": "form" },
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "label",
            { "for": "data-type" },
            "Calculations"
          ),
          React.createElement(
            "select",
            { name: "data-type",
              onChange: this.changeCalc,
              value: this.state.calcType },
            React.createElement(
              "option",
              { value: "_bin", selected: true },
              "To Binary"
            ),
            React.createElement(
              "option",
              { value: "_dec" },
              "To Decimal"
            ),
            React.createElement(
              "option",
              { value: "_hex" },
              "To Hexadecimal"
            ),
            React.createElement(
              "option",
              { value: "add" },
              "Add"
            )
          )
        ),
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "button",
            { type: "add-data", onClick: this.addCalc },
            "Add Step"
          )
        ),
        React.createElement(
          "div",
          { "class": "flex-item" },
          React.createElement(
            "button",
            { onClick: this.clear },
            "Clear All"
          )
        )
      ),
      React.createElement(StepList, { items: this.state.items })
    );
  }

  clear(e) {
    items = [];
    this.setState({ items: items });
  }

  changeBase(e) {
    this.setState({ numericBase: e.target.value });
  }

  changeValue(e) {
    this.setState({ numericValue: e.target.value });
  }
  
  changeCalc(e) {
    this.setState({ calcType: e.target.value });
  }
  
  addCalc(e) {
    e.preventDefault();
    if (this.state.calcType.length === 0) {
      return;
    }
    const newItem = {
      type: "calculation",
      calc: this.state.calcType,
      string: this.state.calcType,
      id: Date.now()
    };
    items = this.state.items.concat(newItem);
    
    this.setState(state => ({
      items: items
    }));
  }

  handleSubmit(e) {
    e.preventDefault();    
    if (this.state.numericValue.length === 0) {
      return;
    }
    const newItem = {
      type: "value",
      numeric: this.state.numericValue,
      base: this.state.numericBase,
      string: this.state.numericValue + " " + this.state.numericBase,
      id: Date.now()
    };
    items = this.state.items.concat(newItem);
    
    this.setState(state => ({
      items: items
    }));
  }
}

class StepList extends React.Component {
  render() {
    return React.createElement(
      "ul",
      null,
      this.props.items.map(item => React.createElement(
        "li",
        { key: item.id },
        item.string
      ))
    );
  }
}

ReactDOM.render(
  React.createElement(AddStep, null),
  document.getElementById('react-placer')
);
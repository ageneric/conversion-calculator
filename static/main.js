"use strict";
class StepPickerApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = { items: [], base: '10', numeric: '', calcType: '2' };

    this.submitNumber = this.submitNumber.bind(this);
    this.submitCalc = this.submitCalc.bind(this);
    this.changeBase = this.changeBase.bind(this);
    this.changeNumeric = this.changeNumeric.bind(this);
    this.changeCalcType = this.changeCalcType.bind(this);
    this.clear = this.clear.bind(this);
  }

  render() {
    // Generated code, read the equivalent in /jsx.
    return React.createElement("div",null,
      React.createElement("div",{"className":"form"},React.createElement("div",{"className":"flex-item"},React.createElement("label",{"htmlFor":"numeric-base"},"Base"),React.createElement("select",{id:"numeric-base",onChange:this.changeBase,value:this.state.base},React.createElement("option",{value:"2"},"Binary"),React.createElement("option",{value:"8"},"Octal"),React.createElement("option",{value:"10"},"Decimal"),React.createElement("option",{value:"16"},"Hexadecimal"),React.createElement("option",{value:"BCD"},"BCD"))),React.createElement("div",{"className":"flex-item"},React.createElement("label",{id:"numeric-digits"},"Digits ",React.createElement("span",{"className":"note"},"(- for negative)")),React.createElement("input",{type:"text",name:"numeric-digits",onChange:this.changeNumeric,value:this.state.numeric})),React.createElement("div",{"className":"flex-item"},React.createElement("button",{onClick:this.submitNumber},"Add Number"))),
      React.createElement("div",{"className":"form"},React.createElement("div",{"className":"flex-item-double"},React.createElement("label",{"htmlFor":"calculation"},"Calculations"),React.createElement("select",{id:"calculation",onChange:this.changeCalcType,value:this.state.calcType},React.createElement("option",{value:"2"},"To Binary"),React.createElement("option",{value:"8"},"To Octal"),React.createElement("option",{value:"10"},"To Decimal"),React.createElement("option",{value:"16"},"To Hexadecimal"),React.createElement("option",{value:"BCD"},"To BCD"),React.createElement("option",{value:"add"},"Add Next"),React.createElement("option",{value:"numerals"},"Display Numerals"),React.createElement("option",{value:"value"},"Display Base 10 Value"),React.createElement("option",{value:"pad_to_bytes"},"Display as Bytes"),React.createElement("option",{value:"sign_and_magnitude"},"Display Sign and Mag."),React.createElement("option",{value:"one_complement"},"Display One's Complement"),React.createElement("option",{value:"two_complement"},"Display Two's Complement"))),React.createElement("div",{"className":"flex-item"},React.createElement("button",{onClick:this.submitCalc},"Add Calculation"))),React.createElement("button",{id:"clear",onClick:this.clear},"Clear All Steps"),React.createElement("p",null,"Modify the list of steps below."),
      React.createElement(StepList,{items:this.state.items})
    );
  }

  // State setters.
  clear(e) {
    this.setState({ items: [] });
  }
  changeBase(e) {
    this.setState({ base: e.target.value });
  }
  changeNumeric(e) {
    this.setState({ numeric: e.target.value });
  }
  changeCalcType(e) {
    this.setState({ calcType: e.target.value });
  }

  submitCalc(e) {
    e.preventDefault();
    if (this.state.calcType.length === 0) {
      return;
    }

    var newItem = {
      type: "calculation",
      calc: this.state.calcType,
      id: Date.now()
    };
    if (this.state.calcType === "add") {
      newItem.string = "Add next number"
    }
    else {
      newItem.string = "Calculation ( -> " + this.state.calcType + " )"
    }

    this.setState((prevState, props) => {
      return {items: prevState.items.concat(newItem)};
    });
  }

  submitNumber(e) {
    e.preventDefault();
    if (this.state.numeric.length === 0) {
      return;
    }

    const newItem = {
      type: "value",
      numeric: this.state.numeric,
      base: this.state.base,
      string: this.state.numeric + " (base " + this.state.base + ")",
      id: Date.now()
    };

    this.setState((prevState, props) => {
      return {items: prevState.items.concat(newItem)};
    });
  }
}

class StepList extends React.Component {
  render() {
    return React.createElement(
      "ul",
      null,
      this.props.items.map(item => React.createElement(
        "li",
        { key: item.id, className: "step" },
        item.string
      ))
    );
  }
}

var stepPicker = ReactDOM.render(
  React.createElement(StepPickerApp, null),
  document.getElementById("step-picker")
);
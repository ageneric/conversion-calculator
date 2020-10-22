var items = [];

function submit() {
  if (items.length == 0) {
    return;
  }
  console.log(items);

  var xhr = new XMLHttpRequest();

  xhr.open('POST', '/result');
  xhr.setRequestHeader('Content-Type', 'application/json;charset=utf-8');
  xhr.onload = function() {
    if (xhr.status === 200 && xhr.responseText !== items) {
      console.log(xhr.responseText);
      response = JSON.parse(xhr.responseText);
      if (response.answer) {
        document.getElementById('final').innerHTML = 'Final value: ' + response.answer;

        document.getElementById('working').innerHTML = '';  // Clear any previous displayed text.
        response.method.forEach(newULElementFromHTML);  // Add each element as a <ul> to working.
      }
      else {
        // Show the caught error message from failed step parsing/execution.
        document.getElementById('final').innerHTML = response.method;
      }
    }
    else if (xhr.status !== 200) {
      alert('Request failed. Returned status of ' + xhr.status);
    }
  };

  xhr.send(JSON.stringify(items));
}

function newULElementFromHTML(htmlString) {
  var ul = document.createElement('ul');
  ul.innerHTML = htmlString;
  document.getElementById('working').appendChild(ul);
}

class AddStep extends React.Component {
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
      React.createElement("div",{"class":"form"},React.createElement("div",{"class":"flex-item"},React.createElement("label",{"for":"numeric-base"},"Base"),React.createElement("select",{id:"numeric-base",onChange:this.changeBase,value:this.state.base},React.createElement("option",{value:"2"},"Binary"),React.createElement("option",{value:"8"},"Octal"),React.createElement("option",{value:"10",selected:true},"Decimal"),React.createElement("option",{value:"16"},"Hexadecimal"),React.createElement("option",{value:"BCD"},"BCD"))),React.createElement("div",{"class":"flex-item"},React.createElement("label",{id:"numeric-digits"},"Digits ",React.createElement("span",{"class":"note"},"(- for negative)")),React.createElement("input",{type:"text",name:"numeric-digits",onChange:this.changeNumeric,value:this.state.numeric})),React.createElement("div",{"class":"flex-item"},React.createElement("button",{onClick:this.submitNumber},"Add Number"))),
      React.createElement("div",{"class":"form"},React.createElement("div",{"class":"flex-item-double"},React.createElement("label",{"for":"calculation"},"Calculations"),React.createElement("select",{id:"calculation",onChange:this.changeCalcType,value:this.state.calcType},React.createElement("option",{value:"2",selected:true},"To Binary"),React.createElement("option",{value:"8"},"To Octal"),React.createElement("option",{value:"10"},"To Decimal"),React.createElement("option",{value:"16"},"To Hexadecimal"),React.createElement("option",{value:"BCD"},"To BCD"),React.createElement("option",{value:"add"},"Add Next"),React.createElement("option",{value:"numerals"},"Display Numerals"),React.createElement("option",{value:"value"},"Display Base 10 Value"),React.createElement("option",{value:"pad_to_bytes"},"Display as Bytes"),React.createElement("option",{value:"sign_and_magnitude"},"Display Sign and Mag."),React.createElement("option",{value:"one_complement"},"Display One's Complement"),React.createElement("option",{value:"two_complement"},"Display Two's Complement"))),React.createElement("div",{"class":"flex-item"},React.createElement("button",{onClick:this.submitCalc},"Add Calculation"))),React.createElement("button",{id:"clear",onClick:this.clear},"Clear All Steps"),React.createElement("p",null,"Modify the list of steps below."),
      React.createElement(StepList,{items:this.state.items})
    );
  }

  clear(e) {
    items = [];
    this.setState({ items: items });
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

    if (this.state.calcType === "add") {
      const newItem = {
        type: "calculation",
        calc: this.state.calcType,
        string: "Add next number",
        id: Date.now()
      };
      items = this.state.items.concat(newItem);
    }
    else {
      const newItem = {
        type: "calculation",
        calc: this.state.calcType,
        string: "Calculation -> " + this.state.calcType,
        id: Date.now()
      };
      items = this.state.items.concat(newItem);
    }

    this.setState(state => ({
      items: items
    }));
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
        { key: item.id, class: "step" },
        item.string
      ))
    );
  }
}

ReactDOM.render(
  React.createElement(AddStep, null),
  document.getElementById('step-picker')
);
"use strict";
class WorkingListApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: props.items};
  }

  componentDidUpdate(prevProps) {
    if (prevProps.items !== this.props.items) {
      this.setState({items: this.props.items});
    }
  }

  render() {
    return React.createElement(
      "div",
      null,
      this.state.items.map(step => React.createElement(
        "ul",
        null,
        step.map(entry => React.createElement(
          entry.tag,
          { key: entry.key, className: entry.class },
          entry.string
        ))
      ))
    );
  }
}

function submit() {
  const items = stepPicker.state.items;
  console.table(items);

  if (items.length == 0) {
    document.getElementById("final").innerHTML = "Please add steps using the inputs above. The result & working will be placed below.";
    workingDisplay.setState({items: []}); // Clears the working display.
    return;
  }

  var xhr = new XMLHttpRequest();

  xhr.open("POST", "/result");
  xhr.setRequestHeader("Content-Type", "application/json;charset=utf-8");
  xhr.onload = function() {
    if (xhr.status === 200 && xhr.responseText !== items) {
      console.log(xhr.responseText);
      var response = JSON.parse(xhr.responseText);

      if (response.answer) {
        document.getElementById("final").innerHTML = "Final value: " + response.answer;
        // Add each method item as a <ul> to the working display.
        console.table(response.method);
        workingDisplay.setState({items: response.method});
      }
      else {
        // Show the caught error message from failed step parsing/execution.
        document.getElementById("final").innerHTML = response.method;
        // Clear the working display.
        workingDisplay.setState({items: []});
      }
    }
    else if (xhr.status !== 200) {
      alert("Request failed. Returned status of " + xhr.status);
    }
  };

  xhr.send(JSON.stringify(items));
}

var workingDisplay = ReactDOM.render(
  React.createElement(WorkingListApp, {items: []}),
  document.getElementById("working")
);
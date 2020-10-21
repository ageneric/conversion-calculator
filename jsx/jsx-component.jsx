//https://infoheap.com/online-react-jsx-to-javascript/
class M {
  constructor(props) {
    super(props);
    this.state = { items: [], numericBase: '', numericValue: '' };
    
    this.handleSubmit = this.handleSubmit.bind(this);
    this.changeBase = this.changeBase.bind(this);
    this.changeValue = this.changeValue.bind(this);
  }

  <div>
    <div class="form">
      <div class="flex-item">
        <label for="data-type">Data Type</label>
        <select name="data-type"
                onChange={this.changeBase}
                value={this.state.numericBase} >
          <option value="bin">Binary</option>
          <option value="oct">Octal</option>
          <option value="dec" selected>Decimal</option>
          <option value="hex">Hexadecimal</option>
          <option value="bcd">BCD</option>
        </select>
      </div>
      <div class="flex-item">
        <label for="data-value">Base 10 Value</label>
        <input name="data-value"
               onChange={this.changeValue}
               value={this.state.numericValue} />
      </div>
      <div class="flex-item">
        <button type="add-data" onClick={this.handleSubmit}>Add Number</button>
      </div>
    </div>
    <div class="form">
      <div class="flex-item">
        <label for="data-type">Calculations</label>
        <select name="data-type"
                onChange={this.changeCalc}
                value={this.state.calcType} >
          <option value="_bin" selected>To Binary</option>
          <option value="_dec">To Decimal</option>
          <option value="_hex">To Hexadecimal</option>
          <option value="add">Add</option>
        </select>
      </div>
      <div class="flex-item">
        <button type="add-data" onClick={this.addCalc}>Add Step</button>
      </div>
      <div class="flex-item">
        <button onClick={this.clear}>Clear All</button>
      </div>
    </div>
    <StepList items={this.state.items} />
  </div>
  
}
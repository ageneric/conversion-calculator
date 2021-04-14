// React JS is generated using:
// https://infoheap.com/online-react-jsx-to-javascript/

    <div>
      <div id="add-step-picker">
        <div id="add-number" class="step-type">
          <div class="form-item">
            <label for="numeric-base">Base</label>
            <select id="numeric-base"
                    onChange={this.changeBase} value={this.state.base}>
              <option value="2">Binary</option>
              <option value="8">Octal</option>
              <option value="10">Decimal</option>
              <option value="16">Hexadecimal</option>
              <option value="BCD">BCD</option>
            </select>
          </div>
          <div class="form-item">
            <label id="numeric-digits">Digits <span class="note">(- for negative)</span></label>
            <input type="text" name="numeric-digits"
                   onChange={this.changeNumeric} value={this.state.numeric} />
          </div>
          <div class="form-item">
            <button name="submit-number" onClick={this.submitNumber}>Create New Number</button>
            <label for="submit-number" id="submit-number"></label>
          </div>
      </div>
        <div id="add-calc" class="step-type">
          <div class="form-item">
            <label for="calculation">Calculations</label>
            <select id="calculation"
                    onChange={this.changeCalcType} value={this.state.calcType}>
              <option value="2">Convert to Binary</option>
              <option value="8">Convert to Octal</option>
              <option value="10">Convert to Decimal</option>
              <option value="16">Convert to Hexadecimal</option>
              <option value="BCD">Convert to BCD</option>
              <option value="add">Add next number</option>
              <option value="numerals">Display as numerals</option>
              <option value="value">Display base 10 value</option>
              <option value="pad_to_bytes">Display padded bytes</option>
              <option value="sign_and_magnitude">Display Sign and Mag.</option>
              <option value="one_complement">Display 1's Complement</option>
              <option value="two_complement">Display 2's Complement</option>
            </select>
          </div>
          <div class="form-item">
            <button name="submit-calc" onClick={this.submitCalc}>Create New Calculation</button>
            <label for="submit-calc" id="submit-calc"></label>
          </div>
        </div>
      </div>
      <button id="clear" onClick={this.clear}>Clear All Steps</button>
      <StepList items={this.state.items} />
    </div>

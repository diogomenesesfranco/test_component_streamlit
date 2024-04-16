import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

interface State {
  numClicks: number
  isFocused: boolean
}
 
class TestComponent extends StreamlitComponentBase<State> {
  public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {
    const name = this.props.args["name"]

    const { theme } = this.props
    const style: React.CSSProperties = {}

    if (theme) {
      const borderStyling = `1px solid ${
        this.state.isFocused ? theme.primaryColor : "gray"
      }`
      style.border = borderStyling
      style.outline = borderStyling
    }
    return (
      <span>
        isso é um teste, {name}! &nbsp;
        <button
          style={style}
          onClick={this.onClicked}
          disabled={this.props.disabled}
          onFocus={this._onFocus}
          onBlur={this._onBlur}
        >
          Clique aqui!
        </button>
      </span>
    )
  }

  private onClicked = (): void => {
    this.setState(
      prevState => ({ numClicks: prevState.numClicks + 1 }),
      () => Streamlit.setComponentValue(this.state.numClicks)
    )
  }

  private _onFocus = (): void => {
    this.setState({ isFocused: true })
  }

  private _onBlur = (): void => {
    this.setState({ isFocused: false })
  }
}

export default withStreamlitConnection(TestComponent)

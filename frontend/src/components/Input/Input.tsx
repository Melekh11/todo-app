import { ChangeEvent, InputHTMLAttributes, memo, useState } from "react";
import "./input.css";

type InputProps = {
  name: string;
  checker: Function;
  changeValue: Function;
} & InputHTMLAttributes<HTMLInputElement>;

const Input = memo(function Input( { 
  disabled, 
  placeholder,
  checker,
  name,
  changeValue,
  } : InputProps) {

    const [ error, setError ] = useState("")
    const [ focused, setFocused ] = useState(false);
    const [ touched, setTouched ] = useState(false);
    const [ value, setValue ] = useState("");

    let inputClassName = "input";
    let placeholderClassName = "input__placeholder";

    const onBlur = (e: ChangeEvent<HTMLInputElement>) => {
      const newError = checker(e.target.value);

      setValue(e.target.value);
      setFocused(false);
      setTouched(true);
      setError(newError);
      changeValue(e.target.value);
    }

    // css logic
    if (focused) {
      placeholderClassName += " input__placeholder_active input__placeholder_blue"
    } else {
      if (error && touched) {
        placeholderClassName += " input__placeholder_red";
        inputClassName += " input_error";
        if (value) {
          placeholderClassName += " input__placeholder_active input__placeholder_red";
        } 
      } else if (!error && value) {
        placeholderClassName += " input__placeholder_active";
      }
    }


    return (
      <label className="input-container" htmlFor={name}>
        <input
          name={name}
          className={inputClassName}
          disabled={disabled}
          onFocus={() => {
            setFocused(true);
          }}
          onBlur={onBlur}
        />
        <span className={placeholderClassName}>{placeholder ?? name}</span>
        {error && touched && <div className="input__error-desc">{error}</div>}
      </label>
    )
 }) ;

export { Input };
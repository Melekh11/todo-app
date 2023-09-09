import { memo, ButtonHTMLAttributes } from "react";
import "./button.css";

type ButtonProps = {
  children?: React.ReactNode
} & ButtonHTMLAttributes<HTMLButtonElement>;

export const Button = memo(function Button({type, onClick, children}: ButtonProps) {
  return (
    <button className={type==="submit" ? "button button_submit" : "button"} onClick={onClick}>
      {children}
    </button>
  );
})

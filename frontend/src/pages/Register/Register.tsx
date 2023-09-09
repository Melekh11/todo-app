import { useState } from "react";
import { Input } from "../../components/Input/Input";
import { Button } from "../../components/Button/Button";
import { useNavigate } from "react-router-dom";
import { routes } from "../../router/router";
import { userService } from "../../services/user";
import { useAppDispatch } from "../../store/store";
import "./register.css";

const checker = (value: string) => {
  if (value.length > 5) return "длинно";
  else return "";
}

export function Register() {

  const [ login, setLogin ] = useState("");
  const [ password, setPassword ] = useState("");
  const [ passwordRepeat, setPasswordRepeat ] = useState("");
  const [ errorMessage, setErrorMessage ] = useState("");
  const navigate = useNavigate();
  const dispatch = useAppDispatch();

  const toLogin = () => navigate(`/${routes.login}`);

  const checkValues = () => {
    const ans = login && password && passwordRepeat && password === passwordRepeat && 
      !checker(password) && !checker(password) && !checker(passwordRepeat);
    return ans;
  }

  const submit = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    
    if ( checkValues() ) {
      setErrorMessage("");
      const data = {login, password};
      userService.register(data)(dispatch)
        .then(() => navigate('/'))
        .catch(err => {
          setErrorMessage(err.toString() ?? "wrong values")
        })
    } else {
      setErrorMessage("wrong values");
    }
  }

  return (
    <form className="register-form">

      <Input
        checker={checker}
        name="login"
        changeValue={setLogin}
      />

      <Input
        name="password"
        checker={checker}
        changeValue={setPassword}
      />

      <Input
        name="passwordRepeat"
        placeholder="repeat password"
        checker={checker}
        changeValue={setPasswordRepeat}
      />

      <div className="register-form__button-keeper">
        <Button onClick={submit} type="submit">register</Button>
        <Button onClick={toLogin}>log in</Button>
      </div>

      {errorMessage && <div className="register-form__error-message">{errorMessage}</div>}
      
    </form>
  )
}

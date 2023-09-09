import { Button } from "../../components/Button/Button";
import { Input } from "../../components/Input/Input";
import { useNavigate } from "react-router-dom";
import { routes } from "../../router/router";
import { useAppDispatch } from "../../store/store";
import { userService } from "../../services/user";
import { useState } from "react";
import "./login.css";

const checker = (value: string) => {
  if (value.length > 5) return "длинно";
  else return "";
}

const Login = () => {

  const [ login, setLogin ] = useState("");
  const [ password, setPassword ] = useState("");
  const [ errorMessage, setErrorMessage ] = useState("");
  const navigate = useNavigate();
  const dispatch = useAppDispatch();

  const checkValues = () => {
    return login && password && !checker(login) && !checker(password);
  }

  const submit = (e : React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();

    if ( checkValues() ) {
      setErrorMessage("");
      const data = {login, password};
      userService.login(data)(dispatch)
        .then(() => navigate('/'))
        .catch((err) => {
          setErrorMessage(err.toString() ?? "wrong values");
        })
    } else setErrorMessage("wrong values");
  }

  const toRegister = () => {navigate(`/${routes.register}`);}

  return (
    <form className="login-form">

      <Input 
        changeValue={setLogin}
        checker={checker}
        name="login"
      />

      <Input
        changeValue={setPassword}
        checker={checker}
        name="password"
      />

      <div className="login-form__button-keeper">
        <Button onClick={submit} type="submit">log in</Button>
        <Button onClick={toRegister}>register</Button>
      </div>

      {errorMessage && <div className="login-form__error-message">{errorMessage}</div>}

    </form>
  )
}

export { Login };

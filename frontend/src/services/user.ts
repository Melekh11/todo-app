import { AppDispatch } from "../store/store";
import { BaseService } from "./base";
import { login  as loginAction } from "../store/reducers/userSlice";

type LoginAction = {
  login: string;
  password: string;
}

type RegisterAction = LoginAction;
const registerAction = loginAction;

class UserService extends BaseService {

  login(data: LoginAction) {
    return (dispatch: AppDispatch) => {
      return fetch(`${this.prefixUrl}/login`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          'Accept': 'application/json',
        },
        body: JSON.stringify(data)
      })
        .then(this.handleErrors)
        .then(res => {
          dispatch(loginAction(data.login));
          return res;
        })
    }
  }

  register(data: RegisterAction) {
    return (dispatch: AppDispatch) => {
      return fetch(`${this.prefixUrl}/auth`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          'Accept': 'application/json',
        },
        body: JSON.stringify(data)
      })
        .then(this.handleErrors)
        .then(res => {
          dispatch(registerAction(data.login))
          return res;
        })
    }
  }

  logout(){}

  getData(){}
}

export const userService = new UserService("users");

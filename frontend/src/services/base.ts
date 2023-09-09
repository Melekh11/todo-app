export class BaseService {

  prefixUrl: string = "http://localhost:1502/";

  constructor(servisePrefix: string) {
    this.prefixUrl += servisePrefix;
  }

  async handleErrors(response: Response) {
    if (!response.ok) {
      const resp = await response.json();
      throw Error(resp.detail);
    }
    return await response.json();
  }
}
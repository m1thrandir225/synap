const baseUrl = process.env.BACKEND_URL;

//TODO: fix if base api url changed
const apiUrl = `${baseUrl}/api/v1`;

export default {
  apiUrl,
  baseUrl,
};

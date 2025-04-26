const baseUrl = import.meta.env.VITE_BACKEND_URL;

//TODO: fix if base api url changed
const apiUrl = `${baseUrl}/api/v1`;

export default {
  apiUrl,
  baseUrl,
};

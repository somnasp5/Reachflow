import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const getResults = async () => {
  const response = await API.get("/results");
  return response.data;
};
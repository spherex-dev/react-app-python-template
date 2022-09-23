import { hello, greeting, echo_post } from "./hello";

test("test_hello", async () => {
  const result = await hello();
  expect(result).toStrictEqual({ hello: "world" });
});

test("test_greeting", async () => {
  const result = await greeting("bob");
  expect(result).toStrictEqual({ greeting: "bob" });
});

test("test_echo", async () => {
  const data = { a: 1, b: 2 };
  const result = await echo_post(data);
  expect(result).toStrictEqual(data);
});

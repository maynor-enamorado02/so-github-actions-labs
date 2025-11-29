describe('CI Pipeline Tests', () => {
  test('Basic arithmetic operation', () => {
    expect(1 + 1).toBe(2);
  });

  test('String manipulation', () => {
    const text = 'CI Pipeline';
    expect(text).toContain('CI');
  });

  test('Async operation simulation', async () => {
    const result = await Promise.resolve('success');
    expect(result).toBe('success');
  });

  test('Object properties', () => {
    const obj = { name: 'CI', status: 'running' };
    expect(obj).toHaveProperty('status');
    expect(obj.status).toBe('running');
  });
});

describe('Environment Tests', () => {
  test('NODE_ENV should be test', () => {
    expect(process.env.NODE_ENV).toBe('test');
  });
});

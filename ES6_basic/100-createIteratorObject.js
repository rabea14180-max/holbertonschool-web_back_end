export default function createIteratorObject(report) {
  const employees = [];

  const allEmployees = report.allEmployees;

  for (const department in allEmployees) {
    employees.push(...allEmployees[department]);
  }

  return employees[Symbol.iterator]();
}

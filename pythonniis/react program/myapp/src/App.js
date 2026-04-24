// function App() {
//   return (
//     <div>
//       <h1>Hello React 🚀</h1>
//       <p>My app is working!</p>
//       <p>My app is not working!</p>
//       <h1>my name is satya pani</h1>
//     </div>
//   );
// }

// export default App;
import React, { useState } from "react";

function App() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [roll, setRoll] = useState("");
  const [marks, setMarks] = useState("");

  // Add student
  const addStudent = () => {
    if (name && roll && marks) {
      const newStudent = { name, roll, marks };
      setStudents([...students, newStudent]);

      setName("");
      setRoll("");
      setMarks("");
    }
  };

  // Delete student
  const deleteStudent = (index) => {
    const newList = students.filter((_, i) => i !== index);
    setStudents(newList);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Student Management System</h1>

      {/* Input Form */}
      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      /><br /><br />

      <input
        type="text"
        placeholder="Enter Roll"
        value={roll}
        onChange={(e) => setRoll(e.target.value)}
      /><br /><br />

      <input
        type="text"
        placeholder="Enter Marks"
        value={marks}
        onChange={(e) => setMarks(e.target.value)}
      /><br /><br />

      <button onClick={addStudent}>Add Student</button>

      {/* Display Table */}
      <h2>Student List</h2>
      <table border="1" style={{ margin: "auto" }}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Roll</th>
            <th>Marks</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {students.map((s, index) => (
            <tr key={index}>
              <td>{s.name}</td>
              <td>{s.roll}</td>
              <td>{s.marks}</td>
              <td>
                <button onClick={() => deleteStudent(index)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestAPI(unittest.TestCase):
    
    # ----------------------
    # Testes para Alunos
    # ----------------------
    def test_adicionar_aluno(self):
        try:
            response = requests.post(f"{BASE_URL}/alunos", json={"nome": "João", "idade": 20})
            self.assertEqual(response.status_code, 201)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_listar_alunos(self):
        try:
            response = requests.get(f"{BASE_URL}/alunos")
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_atualizar_aluno(self):
        try:
            response = requests.put(f"{BASE_URL}/alunos/1", json={"nome": "João Silva", "idade": 21})
            self.assertIn(response.status_code, [200, 404])  # Pode não existir o aluno
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_excluir_aluno(self):
        try:
            response = requests.delete(f"{BASE_URL}/alunos/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_buscar_aluno_por_id(self):
        try:
            response = requests.get(f"{BASE_URL}/alunos/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    # ----------------------
    # Testes para Professores
    # ----------------------
    def test_adicionar_professor(self):
        try:
            response = requests.post(f"{BASE_URL}/professores", json={"nome": "Carlos", "disciplina": "Matemática"})
            self.assertEqual(response.status_code, 201)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_listar_professores(self):
        try:
            response = requests.get(f"{BASE_URL}/professores")
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_atualizar_professor(self):
        try:
            response = requests.put(f"{BASE_URL}/professores/1", json={"nome": "Carlos Souza", "disciplina": "Física"})
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_excluir_professor(self):
        try:
            response = requests.delete(f"{BASE_URL}/professores/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_buscar_professor_por_id(self):
        try:
            response = requests.get(f"{BASE_URL}/professores/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    # ----------------------
    # Testes para Turmas
    # ----------------------
    def test_adicionar_turma(self):
        try:
            response = requests.post(f"{BASE_URL}/turmas", json={"nome": "Turma A", "ano": 2025})
            self.assertEqual(response.status_code, 201)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_listar_turmas(self):
        try:
            response = requests.get(f"{BASE_URL}/turmas")
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_atualizar_turma(self):
        try:
            response = requests.put(f"{BASE_URL}/turmas/1", json={"nome": "Turma B", "ano": 2026})
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_excluir_turma(self):
        try:
            response = requests.delete(f"{BASE_URL}/turmas/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")
    
    def test_buscar_turma_por_id(self):
        try:
            response = requests.get(f"{BASE_URL}/turmas/1")
            self.assertIn(response.status_code, [200, 404])
        except Exception as e:
            self.fail(f"Erro no teste: {e}")

if __name__ == "__main__":
    unittest.main()
1
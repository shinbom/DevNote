# OneToMany, ManyToOne 데코레이터

## OneToMany

```typescript
@OneToMany( () => Report, (report) => report.user)
reports : Report[];
```


```typescript
@ManyToOne( () => User, (user) => user.reports)
reports : User[];
```

첫번쨰 인자에서 `OneToMany, ManyToOne`과 같은 데코레이터를 import한 후, 콜백 함수를 통해 실행하는 이유는 `순환 의존성`때문에 바로 참조할 수 없기 때문이다.

두번째 인자는 TypeORM에서 내부적으로 여러 엔티티간의 관계를 모델링하고 이러한 관계의 설정을 검증함.



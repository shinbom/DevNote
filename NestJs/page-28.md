# 응답 서식 지정하기 & DTO로 속성 변환하기

```
{
    "price": 500000,
    "make": "toyota",
    "model": "corolla",
    "year": 1980,
    "lng": 0,
    "lat": 0,
    "mileage": 100000,
    "user": {
        "id": 19,
        "email": "test1@test.com",
        "password": "a6e2937ca121ebfc.31520218b08b794acb5e0e3c8e189f9b6161a75bccd289b9c002e054926b3642"
    },
    "id": 1
}
```

Response에 암호가 함께 나오고 있다.<br/>
불필요한 정보가 반환되지 않도록, 응답 서식을 지정해야 한다.

## 리포트 DTO 만들기

```typescript
//report.dto.ts
import { Expose, Transform } from 'class-transformer';

export class ReportDto {
  @Expose()
  id: number;
  @Expose()
  price: number;
  @Expose()
  year: number;
  @Expose()
  lng: number;
  @Expose()
  lat: number;
  @Expose()
  make: string;
  @Expose()
  model: string;
  @Expose()
  mileage: number;

  @Transform(({ obj }) => obj.user.id)
  @Expose()
  userId: number;
}
```

`Transform`데코레이터를 통해 속성을 변환한다.

```typescript

@Controller('reports')
export class ReportsController {
  constructor (private reposrtService : ReportsService) {}

  @Post()
  @UseGuards(AuthGuard)
  @Serialize(ReportDto)
  createReport(@Body() body: CreateReportDto, @CurrentUser() user: User) {
    return this.reportsService.create(body, user);
  }
}
```

`Serialize`를 통해 데이터를 변환하여 반환한다.


```
// Response Data

{
    "id": 4,
    "price": 500000,
    "year": 1980,
    "lng": 0,
    "lat": 0,
    "make": "toyotdsafda",
    "model": "corolla",
    "mileage": 100000,
    "userId": 2
}
```